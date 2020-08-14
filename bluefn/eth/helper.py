from eth_utils import from_wei, is_checksum_address, to_checksum_address
from web3 import Web3
from eth_typing import (
    Address,
    BlockNumber,
    ChecksumAddress,
    HexStr,
)

def balance(web3: Web3, address: str):
    end_balance = from_wei(web3.eth.getBalance(address), "ether")
    return end_balance

def role(role_name:str):
    return Web3.soliditySha3(['bytes32'], [role_name.encode()])

def deploy(clz, admin):
    return clz.deploy({'from': admin})

