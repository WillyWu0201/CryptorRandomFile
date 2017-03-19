import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
_IV = os.urandom(16)
_KEY = 'Computer Security Assignment One' #32

def aes_encrypt(data):
    cipher = Cipher(algorithms.AES(_KEY), modes.CBC(_IV), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(str(data)) + encryptor.finalize()
    return ciphertext

def aes_decrypt(data):
    cipher = Cipher(algorithms.AES(_KEY), modes.CBC(_IV), backend=backend)
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(data) + decryptor.finalize()
    return plaintext

encrypt = aes_encrypt("a secret CBC msg")
print (encrypt)
decrypt = aes_decrypt(encrypt)
print (decrypt)