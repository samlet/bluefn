from web3 import Web3

addrs=['0xfe3b557e8fb62b89f4916b721be55ceb828dbd73',
           '0x627306090abaB3A6e1400e9345bC60c78a8BEf57',
           '0xf17f52151EbEF6C7334FAD080c5704D77216b732'
           ]

def local_provider():
    return Web3.HTTPProvider('http://127.0.0.1:8545')

def w3():
    return Web3(local_provider())

def default_accounts():
    return [Web3.toChecksumAddress(addr) for addr in addrs]

def balances(w3):
    return [w3.eth.getBalance(w3_addr) for w3_addr in default_accounts()]

class Besu(object):
    def __init__(self):
        self.w3=w3()
        self.accounts=default_accounts()

    @property
    def balances(self):
        return balances(self.w3)

besu=Besu()



