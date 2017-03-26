# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

import os
from Crypto.Cipher import AES

_IV = os.urandom(16)		# 產生隨機亂數IV
_KEY = os.urandom(32)		# 設定Key
_COUNTER = os.urandom(16)
_BlockSize = AES.block_size # Block Size

#padding
_Pad = lambda s: s + (_BlockSize - len(s) % _BlockSize) * chr(_BlockSize - len(s) % _BlockSize)
_Unpad = lambda s : s[0:-ord(s[-1])]

# 使用CTR加密
def aes_encrypt(data):
    cryptor = AES.new(_KEY, AES.MODE_CTR, counter=lambda: _COUNTER)
    return cryptor.encrypt(_Pad(data))

# 使用CTR解密
def aes_decrypt(data):
    cryptor = AES.new(_KEY, AES.MODE_CTR, counter=lambda: _COUNTER)
    return _Unpad(cryptor.decrypt(data))

# encrypt = aes_encrypt('encrypt this CTR 123123213122131213')
# print (encrypt)
# decrypt = aes_decrypt(encrypt)
# print (decrypt)