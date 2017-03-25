from Crypto.PublicKey import RSA
from Crypto import Random
import random, string

_RANDOM = Random.new().read
_KEY = RSA.generate(2048, _RANDOM)  # generate pub and priv key
_PUBLICKEY = _KEY.publickey()  # pub key export for exchange

_BlockSize = 16
_Pad = lambda s: s + (_BlockSize - len(s) % _BlockSize) * chr(_BlockSize - len(s) % _BlockSize)
_Unpad = lambda s : s[0:-ord(s[-1])]

# encrypted code below
def rsa_encrypt(data):
    encrypted = _PUBLICKEY.encrypt(_Pad(data), 16)
    return encrypted

# decrypted code below
def rsa_decrypt(data):
    decrypted = _KEY.decrypt(data)
    return _Unpad(decrypted)

# text = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(1 * 1024 * 1024 + 7))
# encrypt = rsa_encrypt(text)
# print (encrypt)
# decrypt = rsa_decrypt(encrypt)
# print (decrypt)
