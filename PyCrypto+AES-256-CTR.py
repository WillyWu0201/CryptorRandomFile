# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

import os
from Crypto.Cipher import AES

_IV = os.urandom(16)
_KEY = os.urandom(16)
_COUNTER = os.urandom(16)
_BlockSize = AES.block_size
_Pad = lambda s: s + (_BlockSize - len(s) % _BlockSize) * chr(_BlockSize - len(s) % _BlockSize)
_Unpad = lambda s : s[0:-ord(s[-1])]

def aes_encrypt(data, key):
    cryptor = AES.new(key, AES.MODE_CTR, counter=lambda: _COUNTER)
    return cryptor.encrypt(_Pad(data))


def aes_decrypt(data, key):
    cryptor = AES.new(key, AES.MODE_CTR, counter=lambda: _COUNTER)
    return _Unpad(cryptor.decrypt(data))


# def counter_callback():
#     self.cnter_cb_called += 1
#     return self.secret[self.cnter_cb_called % AES.block_size] * AES.block_size

encrypt = aes_encrypt('encrypt this CTR 123123213122131213', _KEY)
print (encrypt)
decrypt = aes_decrypt(encrypt, _KEY)
print (decrypt)