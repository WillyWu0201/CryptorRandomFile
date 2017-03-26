# -*- coding: utf-8 -*-
import time
import GenerateRamdomStringFile

import PyCrypto_AES_256_ECB
import PyCrypto_AES_256_CBC
import PyCrypto_AES_256_CTR
# import PyCrypo_RSA_2048
import PyCrypo_SHA_512

import Cryptography_AES_256_ECB
import Cryptography_AES_256_CBC
import Cryptography_AES_256_CTR
# import Cryptography_RSA_2048
import Cryptography_SHA_512

_FILESIZE = 1024 * 1024 + 7

print ('Generate Ramdom String File')
start = time.time()
# GenerateRamdomStringFile.generateStringFile(_FILESIZE)
file = open("RandomString.txt")
plaintext = file.readline()
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')

# PyCrypto_AES_256_ECB
print ('PyCrypto_AES_256_ECB')
start = time.time()
encrypt = PyCrypto_AES_256_ECB.aes_encrypt(plaintext)
# print (encrypt)
decrypt = PyCrypto_AES_256_ECB.aes_decrypt(encrypt)
# print (decrypt)
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')

# Cryptography_AES_256_ECB
print ('Cryptography_AES_256_ECB')
start = time.time()
encrypt = Cryptography_AES_256_ECB.aes_encrypt(plaintext)
# print (encrypt)
decrypt = Cryptography_AES_256_ECB.aes_decrypt(encrypt)
# print (decrypt)
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')

# PyCrypto_AES_256_CBC
print ('PyCrypto_AES_256_CBC')
start = time.time()
encrypt = PyCrypto_AES_256_CBC.aes_encrypt(plaintext)
# print (encrypt)
decrypt = PyCrypto_AES_256_CBC.aes_decrypt(encrypt)
# print (decrypt)
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')

# Cryptography_AES_256_CBC
print ('Cryptography_AES_256_CBC')
start = time.time()
encrypt = Cryptography_AES_256_CBC.aes_encrypt(plaintext)
# print (encrypt)
decrypt = Cryptography_AES_256_CBC.aes_decrypt(encrypt)
# print (decrypt)
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')

# PyCrypto_AES_256_CTR
print ('PyCrypto_AES_256_CTR')
start = time.time()
encrypt = PyCrypto_AES_256_CTR.aes_encrypt(plaintext)
# print (encrypt)
decrypt = PyCrypto_AES_256_CTR.aes_decrypt(encrypt)
# print (decrypt)
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')

# Cryptography_AES_256_CTR
print ('Cryptography_AES_256_CTR')
start = time.time()
encrypt = Cryptography_AES_256_CTR.aes_encrypt(plaintext)
# print (encrypt)
decrypt = Cryptography_AES_256_CTR.aes_decrypt(encrypt)
# print (decrypt)
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')

# PyCrypo_SHA_512
print ('PyCrypo_SHA_512')
start = time.time()
hash = PyCrypo_SHA_512.hashSHA512(plaintext)
# print (hash)
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')

# Cryptography_SHA_512
print ('Cryptography_SHA_512')
start = time.time()
hash = Cryptography_SHA_512.hashSHA512(plaintext)
# print (hash)
end = time.time()
elapsed = end - start
print ('Time taken: ' + str(elapsed) + 'seconds.')

# # PyCrypo_RSA_2048
# print ('PyCrypo_RSA_2048')
# start = time.time()
# encrypt = PyCrypo_RSA_2048.rsa_encrypt(plaintext)
# # print (encrypt)
# decrypt = PyCrypo_RSA_2048.rsa_decrypt(encrypt)
# # print (decrypt)
# end = time.time()
# elapsed = end - start
# print ('Time taken: ' + str(elapsed) + 'seconds.')
#
# # Cryptography_RSA_2048
# print ('Cryptography_RSA_2048')
# start = time.time()
# encrypt = Cryptography_RSA_2048.rsa_encrypt(plaintext)
# # print (encrypt)
# decrypt = Cryptography_RSA_2048.rsa_decrypt(encrypt)
# # print (decrypt)
# end = time.time()
# elapsed = end - start
# print ('Time taken: ' + str(elapsed) + 'seconds.')

