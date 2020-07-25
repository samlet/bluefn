"""
$ pytest -s -v test_contract_v2.py
"""
import pytest
import os
import logging

logger = logging.getLogger(__name__)

from web3 import (
    EthereumTesterProvider,
    Web3,
)


@pytest.fixture
def tester_provider():
    return EthereumTesterProvider()


@pytest.fixture
def eth_tester(tester_provider):
    return tester_provider.ethereum_tester


@pytest.fixture
def w3(tester_provider):
    return Web3(tester_provider)


@pytest.fixture
def foo_contract(eth_tester, w3):
    from bluefn.utils.contracts_util import compile_contract

    logger.info("current dir: %s", os.getcwd())

    deploy_address = eth_tester.get_accounts()[0]
    abi, bytecode= compile_contract('../contracts/foo.sol')
    # Create our contract class.
    FooContract = w3.eth.contract(abi=abi, bytecode=bytecode)
    # issue a transaction to deploy the contract.
    tx_hash = FooContract.constructor().transact({
        'from': deploy_address,
    })
    # wait for the transaction to be mined
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, 180)
    # instantiate and return an instance of our contract.
    return FooContract(tx_receipt.contractAddress)

def test_initial_greeting(foo_contract):
    hw = foo_contract.caller.bar()
    assert hw == "hello world"


def test_can_update_greeting(w3, foo_contract):
    # send transaction that updates the greeting
    tx_hash = foo_contract.functions.setBar(
        "testing contracts is easy",
    ).transact({
        'from': w3.eth.accounts[1],
    })
    w3.eth.waitForTransactionReceipt(tx_hash, 180)

    # verify that the contract is now using the updated greeting
    hw = foo_contract.caller.bar()
    assert hw == "testing contracts is easy"


def test_updating_greeting_emits_event(w3, foo_contract):
    # send transaction that updates the greeting
    tx_hash = foo_contract.functions.setBar(
        "testing contracts is easy",
    ).transact({
        'from': w3.eth.accounts[1],
    })
    receipt = w3.eth.waitForTransactionReceipt(tx_hash, 180)

    # get all of the `barred` logs for the contract
    logs = foo_contract.events.barred.getLogs()
    assert len(logs) == 1

    # verify that the log's data matches the expected value
    event = logs[0]
    assert event.blockHash == receipt.blockHash
    assert event.args._bar == "testing contracts is easy"

