from Crypto.Cipher import AES
from Crypto import Random

key = "This is a key123"

def encrypt(string):
    iv = Random.new().read(AES.block_size)
    aes = AES.new(key, AES.MODE_CFB, iv)
    return aes.encrypt(string)

def decrypt(string):
    iv = Random.new().read(AES.block_size)
    aes = AES.new(key, AES.MODE_CFB, iv)
    return aes.decrypt(string)
