import hashlib
import hmac
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class AdvancedEncryption:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.backend = default_backend()

    def encrypt(self, plaintext):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=self.backend)
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext) + padder.finalize()
        return encryptor.update(padded_data) + encryptor.finalize()

    def decrypt(self, ciphertext):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=self.backend)
        decryptor = cipher.decryptor()
        decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(decrypted_padded_data) + unpadder.finalize()

    def generate_key(self):
        return os.urandom(32)

    def generate_iv(self):
        return os.urandom(16)

    def hmac_sha256(self, message):
        return hmac.new(self.key, message, hashlib.sha256).digest()

# Example usage
key = AdvancedEncryption.generate_key()
iv = AdvancedEncryption.generate_iv()
encryption = AdvancedEncryption(key, iv)

plaintext = b"Hello, Cosmic Pi Network!"
ciphertext = encryption.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decrypted_text = encryption.decrypt(ciphertext)
print("Decrypted Text:", decrypted_text)

message = b"Hello, Cosmic Pi Network!"
hmac = encryption.hmac_sha256(message)
print("HMAC:", hmac)
