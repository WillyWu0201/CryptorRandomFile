# -*- coding: utf-8 -*-
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

backend = default_backend()

def hashSHA512(data):
    digest = hashes.Hash(hashes.SHA512(), backend=default_backend())
    digest.update(data)
    return digest.finalize()


# hash = hashSHA512('encrypt this SHA512 123123213122131213')
# print (hash)