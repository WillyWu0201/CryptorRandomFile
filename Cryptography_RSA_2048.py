from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import random, string

_PRIVATEKEY = rsa.generate_private_key(
    public_exponent=65537,
    key_size=1024*1024,
    backend=default_backend()
)
_PUBLICKEY = _PRIVATEKEY.public_key()

def rsa_encrypt(data):
    ciphertext = _PUBLICKEY.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA512()),
            algorithm=hashes.SHA512(),
            label=None
        )
    )
    return ciphertext

def rsa_decrypt(data):
    plaintext = _PRIVATEKEY.decrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA512()),
            algorithm=hashes.SHA512(),
            label=None
        )
    )
    return plaintext

# text = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(1 * 1024 * 1024 + 7))
# encrypt = rsa_encrypt(text)
# print (encrypt)
# decrypt = rsa_decrypt(encrypt)
# print (decrypt)