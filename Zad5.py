from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad

with open('plik.txt', 'rb') as f:
    ciphered_data = f.read()

password = 'dobrehaselko'
salt = b'DRw\xaaj_\xfb\xca\xec\x91\xcd \xd9xk\x88\xe0\xbd\x97\xcab-\xe9\xa7D ^\xee\x93\xac\x92\x1f'
key = PBKDF2(password, salt, dkLen=32)

""" Tu pisz swój kod """
#cipher = 
#original_data = 
""""""
print(original_data)
