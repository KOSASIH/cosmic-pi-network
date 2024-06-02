import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

class Crypto:
    def __init__(self):
        pass

    def generate_key_pair(self):
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        return key

    def encrypt_data(self, key, data):
        cipher = serialization.load_pem_private_key(key, password=None)
        encrypted_data = cipher.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_data

    def decrypt_data(self, key, encrypted_data):
        cipher = serialization.load_pem_private_key(key, password=None)
        decrypted_data = cipher.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_data

# Example usage
crypto = Crypto()
key = crypto.generate_key_pair()
data = b"Hello, World!"
encrypted_data = crypto.encrypt_data(key, data)
print("Encrypted data:", encrypted_data)
decrypted_data = crypto.decrypt_data(key, encrypted_data)
print("Decrypted data:", decrypted_data)
