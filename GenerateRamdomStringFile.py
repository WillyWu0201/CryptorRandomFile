# -*- coding: utf-8 -*-
import random, string

#隨機產生大小為size的字串檔案
def generateStringFile(size):
    text = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(size))
    file = open('RandomString.txt', 'wb')
    file.write(text)


# _FILESIZE = 1024
# generateStringFile(_FILESIZE)

