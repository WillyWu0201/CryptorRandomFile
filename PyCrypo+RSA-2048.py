from Crypto.PublicKey import RSA
from Crypto import Random
# import ast

_RANDOM = Random.new().read
_KEY = RSA.generate(2048, _RANDOM)  # generate pub and priv key
_PUBLICKEY = _KEY.publickey()  # pub key export for exchange


# message to encrypt is in the above line 'encrypt this message'
def rsa_encrypt(data, key):
    encrypted = _PUBLICKEY.encrypt(str(data), 32)
    return encrypted


# decrypted code below
def rsa_decrypt(data, key):
    # decrypted = key.decrypt(ast.literal_eval(str(data))) # this line need import ast
    decrypted = key.decrypt(data)
    return decrypted


encrypt = rsa_encrypt('encrypt this RSA-2048', _KEY)
print (encrypt)
decrypt = rsa_decrypt(encrypt, _KEY)
print (decrypt)
