# coding=utf-8
from Crypto.Hash import SHA256
hash = SHA256.new()
hash.update(b'message')
h = hash.digest()
h2 = hash.hexdigest()
print(h)
print(h2)