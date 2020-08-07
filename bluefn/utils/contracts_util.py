from web3 import Web3
from solcx import compile_source

def compile_source_file(file_path):
   with open(file_path, 'r') as f:
      source = f.read()

   return compile_source(source)

def deploy_contract(w3, contract_interface):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).constructor().transact()

    address = w3.eth.getTransactionReceipt(tx_hash)['contractAddress']
    return address

def deploy(w3, file_path):
    compiled_sol = compile_source_file(file_path)
    contract_id, contract_interface = compiled_sol.popitem()
    address = deploy_contract(w3, contract_interface)
    return contract_id, contract_interface, address

def compile_contract(file_path):
    compiled_sol = compile_source_file(file_path)
    contract_id, contract_interface = compiled_sol.popitem()
    return contract_interface['abi'], contract_interface['bin']

