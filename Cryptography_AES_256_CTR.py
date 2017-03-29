# -*- coding: utf-8 -*-
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
_IV = os.urandom(16)    # 產生隨機亂數IV
_KEY = os.urandom(32)	# 設定Key
_BlockSize = 16	        # Block Size

#padding
_Pad = lambda s: s + (_BlockSize - len(s) % _BlockSize) * chr(_BlockSize - len(s) % _BlockSize)
_Unpad = lambda s : s[0:-ord(s[-1])]

# 使用CTR加密
def aes_encrypt(data):
    cipher = Cipher(algorithms.AES(_KEY), modes.CTR(_IV), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(_Pad(data))
    return ciphertext

# 使用CTR解密
def aes_decrypt(data):
    cipher = Cipher(algorithms.AES(_KEY), modes.CTR(_IV), backend=backend)
    decryptor = cipher.decryptor()
    plaintext = _Unpad(decryptor.update(data))
    return plaintext

# encrypt = aes_encrypt("a secret CTR msg 98765432123456789098765")
# print (encrypt)
# decrypt = aes_decrypt(encrypt)
# print (decrypt)