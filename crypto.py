import hashlib
import os
from typing import Tuple

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, rsa, ec
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Hash functions
def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()

def sha512(data: bytes) -> bytes:
    return hashlib.sha512(data).digest()

def blake2b(data: bytes) -> bytes:
    return hashlib.blake2b(data).digest()

# Digital signatures
def generate_ed25519_keypair() -> Tuple[ed25519.Ed25519PrivateKey, ed25519.Ed25519PublicKey]:
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

def sign_ed25519(private_key: ed25519.Ed25519PrivateKey, msg: bytes) -> bytes:
    return private_key.sign(msg)

def verify_ed25519(public_key: ed25519.Ed25519PublicKey, msg: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(signature, msg)
        return True
    except (ed25519.InvalidSignature, ValueError):
        return False

def generate_rsa_keypair(key_size: int = 2048) -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_rsa(private_key: rsa.RSAPrivateKey, msg: bytes) -> bytes:
    signature = private_key.sign(
        msg,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return signature

def verify_rsa(public_key: rsa.RSAPublicKey, msg: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(
            signature,
            msg,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except (rsa.VerificationError, ValueError):
        return False

def generate_ec_keypair(curve: str = "secp256k1") -> Tuple[ec.EllipticCurvePrivateKey, ec.EllipticCurvePublicKey]:
    curve = ec.SECP256K1() if curve == "secp256k1" else ec.SECP384R1()
    private_key = ec.generate_private_key(curve)
    public_key = private_key.public_key()
    return private_key, public_key

def sign_ec(private_key: ec.EllipticCurvePrivateKey, msg: bytes) -> bytes:
    signature = private_key.sign(
        msg,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_ec(public_key: ec.EllipticCurvePublicKey, msg: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(
            signature,
            msg,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except (ec.ECDSAError, ValueError):
        return False

# Encryption
def generate_aes_key(key_size: int = 256) -> bytes:
    return os.urandom(key_size // 8)

def encrypt_aes_ctr(key: bytes, data: bytes) -> bytes:
    nonce = os.urandom(16)
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.CTR(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return nonce + ciphertext

def decrypt_aes_ctr(key: bytes, ciphertext: bytes) -> bytes:
    nonce = ciphertext[:16]
    ciphertext = ciphertext[16:]
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.CTR(nonce), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

def encrypt_aes_gcm(key: bytes, data: bytes) -> bytes:
    nonce = os.urandom(12)
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.GCM(nonce, tag=None), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return nonce + ciphertext + encryptor.tag

def decrypt_aes_gcm(key: bytes, ciphertext: bytes) -> bytes:
    nonce = ciphertext[:12]
    ciphertext = ciphertext[12:-16]
    tag = ciphertext[-16:]
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.GCM(nonce, tag=tag, nonce_size=12), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

# Key derivation
def derive_key_pbkdf2(password: bytes, salt: bytes, key_size: int = 32) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=key_size // 8,
        salt=salt,
        iterations=100000
    )
    return kdf.derive(password)

if __name__ == "__main__":
    # Example usage
    private_key, public_key = generate_ed25519_keypair()
    msg = b"Hello, world!"
    signature = sign_ed25519(private_key, msg)
    print(f"Signature: {signature.hex()}")
    print(f"Verification: {verify_ed25519(public_key, msg, signature)}")

    private_key, public_key = generate_rsa_keypair()
    msg = b"Hello, world!"
    signature = sign_rsa(private_key, msg)
    print(f"Signature: {signature.hex()}")
    print(f"Verification: {verify_rsa(public_key, msg, signature)}")

    private_key, public_key = generate_ec_keypair()
    msg = b"Hello, world!"
    signature = sign_ec(private_key, msg)
    print(f"Signature: {signature.hex()}")
    print(f"Verification: {verify_ec(public_key, msg, signature)}")

    key = generate_aes_key()
    data = b"Hello, world!"
    ciphertext = encrypt_aes_ctr(key, data)
    print(f"Ciphertext: {ciphertext.hex()}")
    plaintext = decrypt_aes_ctr(key, ciphertext)
    print(f"Plaintext: {plaintext.decode()}")

    ciphertext = encrypt_aes_gcm(key, data)
    print(f"Ciphertext: {ciphertext.hex()}")
    plaintext = decrypt_aes_gcm(key, ciphertext)
    print(f"Plaintext: {plaintext.decode()}")

    password = b"password"
    salt = os.urandom(16)
    key = derive_key_pbkdf2(password, salt)
    print(f"Key: {key.hex()}")
