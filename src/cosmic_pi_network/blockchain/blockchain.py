import hashlib
from ecdsa import SigningKey, VerifyingKey

class Blockchain:
    def __init__(self):
        pass

    def create_block(self, transactions, previous_block_hash):
        block = {
            'transactions': transactions,
            'previous_block_hash': previous_block_hash,
            'timestamp': datetime.datetime.now().timestamp(),
            'nonce': 0
        }
        block_hash = self.calculate_block_hash(block)
        return block, block_hash

    def calculate_block_hash(self, block):
        block_string = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def validate_block(self, block, previous_block_hash):
        if block['previous_block_hash']!= previous_block_hash:
            return False
        block_hash = self.calculate_block_hash(block)
        if block_hash!= block['hash']:
            return False
        return True

    def add_block(self, block, blockchain):
        if self.validate_block(block, blockchain[-1]['hash']):
            blockchain.append(block)
            return True
        return False
