# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

import os
from Crypto.Cipher import AES

_KEY = os.urandom(32)		# 設定Key
_BlockSize = AES.block_size	# Block Size

#padding
_Pad = lambda s: s + (_BlockSize - len(s) % _BlockSize) * chr(_BlockSize - len(s) % _BlockSize)
_Unpad = lambda s : s[0:-ord(s[-1])]

# 使用ECB加密
def aes_encrypt(data):
    cryptor = AES.new(_KEY, AES.MODE_ECB)
    return cryptor.encrypt(_Pad(data))

# 使用ECB解密
def aes_decrypt(data):
    cryptor = AES.new(_KEY, AES.MODE_ECB)
    return _Unpad(cryptor.decrypt(data))

# encrypt = aes_encrypt('encrypt this ECB 098765456789')
# print (encrypt)
# decrypt = aes_decrypt(encrypt)
# print (decrypt)