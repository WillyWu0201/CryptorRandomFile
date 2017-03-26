# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

import os
import random, string
from Crypto.Cipher import AES

_IV = os.urandom(16)
_KEY = os.urandom(32)
_BlockSize = AES.block_size
_Pad = lambda s: s + (_BlockSize - len(s) % _BlockSize) * chr(_BlockSize - len(s) % _BlockSize)
_Unpad = lambda s : s[0:-ord(s[-1])]

def aes_encrypt(data):
    cryptor = AES.new(_KEY, AES.MODE_CBC, _IV)
    return cryptor.encrypt(_Pad(data))

def aes_decrypt(data):
    cryptor = AES.new(_KEY, AES.MODE_CBC, _IV)
    return _Unpad(cryptor.decrypt(data))

# plainText = generateString()
# encrypt = aes_encrypt(plainText)
# print (encrypt)
# decrypt = aes_decrypt(encrypt)
# print (decrypt)


