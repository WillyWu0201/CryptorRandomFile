# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals

from Crypto.Hash import SHA512

def hashSHA512(data):
    hash = SHA512.new()
    hash.update(data)
    return hash.hexdigest()

# hash = hashSHA512('encrypt this SHA512 123123213122131213')
# print (hash)