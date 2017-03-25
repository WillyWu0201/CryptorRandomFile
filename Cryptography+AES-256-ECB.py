import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

backend = default_backend()
_KEY = os.urandom(16)
_BlockSize = 16
_Pad = lambda s: s + (_BlockSize - len(s) % _BlockSize) * chr(_BlockSize - len(s) % _BlockSize)
_Unpad = lambda s : s[0:-ord(s[-1])]

def aes_encrypt(data):
    cipher = Cipher(algorithms.AES(_KEY), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(_Pad(data))
    return ciphertext

def aes_decrypt(data):
    cipher = Cipher(algorithms.AES(_KEY), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    plaintext = _Unpad(decryptor.update(data))  # + decryptor.finalize()
    return plaintext

# with open('output_file', 'wb') as fout:
#     fout.write(os.urandom((1024 * 1024 * 512) * 8) + 7) # replace 1024 with size_kb if not unreasonably large

encrypt = aes_encrypt("a secret ECB msg 098765434567fewe890")
print (encrypt)
decrypt = aes_decrypt(encrypt)
print (decrypt)