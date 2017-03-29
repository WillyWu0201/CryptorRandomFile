# -*- coding: utf-8 -*-
import time
import random, string

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

_PRIVATEKEY = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
_PUBLICKEY = _PRIVATEKEY.public_key()

_BlockSize = 16
_Pad = lambda s: s + (_BlockSize - len(s) % _BlockSize) * chr(_BlockSize - len(s) % _BlockSize)
_Unpad = lambda s : s[0:-ord(s[-1])]

def rsa_encrypt(data):
    ciphertext = _PUBLICKEY.encrypt(
        data,
        # _Pad(data),
        padding.PKCS1v15()
        # padding.OAEP(
        #     mgf=padding.MGF1(algorithm=hashes.SHA1()),
        #     algorithm=hashes.SHA1(),
        #     label=None
        # )
    )
    return ciphertext

def rsa_decrypt(data):
    plaintext = _PRIVATEKEY.decrypt(
        data,
        padding.PKCS1v15()
        # padding.OAEP(
        #     mgf=padding.MGF1(algorithm=hashes.SHA1()),
        #     algorithm=hashes.SHA1(),
        #     label=None
        # )
    )
    return plaintext

start = time.time()
plaintext = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(240))
encrypt = rsa_encrypt(plaintext)
# print (encrypt)
# decrypt = rsa_decrypt(encrypt)
# print (decrypt)
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')