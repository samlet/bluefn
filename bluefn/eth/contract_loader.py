import os
import logging

logger = logging.getLogger(__name__)

class ContractLoader(object):
    def __init__(self, provider='tester'):
        from web3 import (
            EthereumTesterProvider,
            Web3,
        )
        if provider=='tester':
            provider=EthereumTesterProvider()
            self.eth_tester=provider.ethereum_tester
        else:
            # doesn't work
            provider=Web3.HTTPProvider('http://127.0.0.1:8545')
            self.eth_tester = provider.eth
        self.w3=Web3(provider)

    @property
    def connected(self):
        return self.w3.isConnected()

    def contract(self, file):
        from bluefn.utils.contracts_util import compile_contract

        logger.info("current dir: %s", os.getcwd())

        deploy_address = self.eth_tester.get_accounts()[0]
        abi, bytecode = compile_contract(file)
        # Create our contract class.
        Contract = self.w3.eth.contract(abi=abi, bytecode=bytecode)
        # issue a transaction to deploy the contract.
        tx_hash = Contract.constructor().transact({
            'from': deploy_address,
        })
        # wait for the transaction to be mined
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash, timeout=180)
        # instantiate and return an instance of our contract.
        return Contract(tx_receipt.contractAddress)

