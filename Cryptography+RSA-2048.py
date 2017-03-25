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

def aes_encrypt(data):
    ciphertext = _PUBLICKEY.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    return ciphertext

def aes_decrypt(data):
    plaintext = _PRIVATEKEY.decrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    return plaintext

encrypt = aes_encrypt("a secret RSA msg newjovnowe989765667890898voioejvoie")
print (encrypt)
decrypt = aes_decrypt(encrypt)
print (decrypt)