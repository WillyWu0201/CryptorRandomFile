from Crypto.PublicKey import RSA
from Crypto import Random
# import ast

_RANDOM = Random.new().read
_KEY = RSA.generate(2048, _RANDOM)  # generate pub and priv key
_PUBLICKEY = _KEY.publickey()  # pub key export for exchange

_BlockSize = 16
_Pad = lambda s: s + (_BlockSize - len(s) % _BlockSize) * chr(_BlockSize - len(s) % _BlockSize)
_Unpad = lambda s : s[0:-ord(s[-1])]


# encrypted code below
def rsa_encrypt(data, key):
    encrypted = _PUBLICKEY.encrypt(_Pad(data), 32)
    return encrypted


# decrypted code below
def rsa_decrypt(data, key):
    decrypted = key.decrypt(data)
    return _Unpad(decrypted)


encrypt = rsa_encrypt('encrypt this RSA-2048 222jfi32jfi32jf82v22222', _KEY)
print (encrypt)
decrypt = rsa_decrypt(encrypt, _KEY)
print (decrypt)
