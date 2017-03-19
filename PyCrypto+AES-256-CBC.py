# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

import os
from Crypto.Cipher import AES

_IV = os.urandom(16)
_KEY = 'Computer Security Assignment One' #32

#generte random file
# with open('output_file', 'wb') as fout:
#     fout.write(os.urandom(536870913)) # size_kb

def aes_encrypt(data, key):
    cryptor = AES.new(key, AES.MODE_CBC, _IV)
    return cryptor.encrypt(data)


def aes_decrypt(data, key):
    cryptor = AES.new(key, AES.MODE_CBC, _IV)
    return cryptor.decrypt(data)

encrypt = aes_encrypt('encrypt this CBC', _KEY)
print (encrypt)
decrypt = aes_decrypt(encrypt, _KEY)
print (decrypt)


