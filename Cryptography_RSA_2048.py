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
    for text in data:
        cipher = _PUBLICKEY.encrypt(
        text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
            )
        )

start = time.time()
plaintext = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(512 * 1024 * 1024 + 7))
encrypt = rsa_encrypt(plaintext)
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')