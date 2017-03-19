# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

from Crypto.Cipher import AES

_IV = 16 * '\x00'
_KEY = 'Computer Security Assignment One'

def aes_encrypt(data, key):
    cryptor = AES.new(key, AES.MODE_ECB, _IV)
    return cryptor.encrypt(data)


def aes_decrypt(data, key):
    cryptor = AES.new(key, AES.MODE_ECB, _IV)
    return cryptor.decrypt(data)

encrypt = aes_encrypt('encrypt this ECB', _KEY)
print (encrypt)
decrypt = aes_decrypt(encrypt, _KEY)
print (decrypt)