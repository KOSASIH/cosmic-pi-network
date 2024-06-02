# src/cosmic_pi_network/blockchain/smart_contracts.py
import web3

class SmartContract:
    def __init__(self, contract_address, abi):
        self.contract = web3.eth.contract(address=contract_address, abi=abi)

    def deploy(self):
        tx_hash = self.contract.constructor().transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt.contractAddress

    def call(self, function_name, *args):
        return self.contract.functions[function_name](*args).call()
