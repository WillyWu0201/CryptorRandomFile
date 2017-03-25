# -*- coding: utf-8 -*-
import os
import random, string

def generateStringFile(size):
    text = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(size))
    file = open('RandomString.txt', 'wb')
    file.write(text)

