# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

import os
from Crypto.Cipher import AES

_IV = os.urandom(16)
_KEY = 'Computer Security Assignment One'
_COUNTER = os.urandom(16)

def aes_encrypt(data, key):
    cryptor = AES.new(key, AES.MODE_CTR, counter=lambda: _COUNTER)
    return cryptor.encrypt(data)


def aes_decrypt(data, key):
    cryptor = AES.new(key, AES.MODE_CTR, counter=lambda: _COUNTER)
    return cryptor.decrypt(data)

# def counter_callback():
#     self.cnter_cb_called += 1
#     return self.secret[self.cnter_cb_called % AES.block_size] * AES.block_size

encrypt = aes_encrypt('encrypt this CTR', _KEY)
print (encrypt)
decrypt = aes_decrypt(encrypt, _KEY)
print (decrypt)