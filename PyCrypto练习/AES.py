# coding=utf-8
from Crypto.Cipher import AES
#加密
obj = AES.new('This is a key123',AES.MODE_CBC,'This is an IV456')
message = 'The answer is no'
ciphertext = obj.encrypt(message)
print(ciphertext)
'''
'This is a key123'为key,长度有严格的要求，必须为16，24或32位
'This is an IV456'为IV，长度只能是16位
'''
#解密
obj2 = AES.new('This is a key123',AES.MODE_CBC,'This is an IV456')
s = obj2.decrypt(ciphertext)
print(s)
#必须知道key和IV才能解密


pad = lambda s:s+(16-len(s)%16)*chr(16-len(s)%16)
print(pad('ab'),123)
print(10*chr(14),456)
print(8-4%16)
