# -*- coding: utf-8 -*-
import time
import random, string

from Crypto.PublicKey import RSA
from Crypto import Random

_RANDOM = Random.new().read
_KEY = RSA.generate(2048, _RANDOM)  # generate pub and priv key
_PUBLICKEY = _KEY.publickey()  # pub key export for exchange

_BlockSize = 16
_Pad = lambda s: s + (_BlockSize - len(s) % _BlockSize) * chr(_BlockSize - len(s) % _BlockSize)
_Unpad = lambda s: s[0:-ord(s[-1])]


# 使用RSA加密
def rsa_encrypt(data):
    encrypted = _PUBLICKEY.encrypt(_Pad(data), 16)
    return encrypted

# 使用RSA解密
def rsa_decrypt(data):
    decrypted = _KEY.decrypt(data)
    return _Unpad(decrypted)

start = time.time()
encrypt = rsa_encrypt(''.join(random.choice(string.ascii_letters + string.digits) for x in range(512 * 1024 * 1024 + 7)))
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')
