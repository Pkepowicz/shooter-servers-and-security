from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad

class Encryptor:

    def __init__(self, password=''):
        self.password=password

    def encrypt(self, data, password=''):
        if password == '':
            password = self.password

        salt = b'DRw\xaaj_\xfb\xca\xec\x91\xcd \xd9xk\x88\xe0\xbd\x97\xcab-\xe9\xa7D ^\xee\x93\xac\x92\x1f'
        key = PBKDF2(password, salt, dkLen=32, count=1000000)
        
        cipher = AES.new(key, AES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad(data, AES.block_size))

        return ciphered_data

    def decrypt(self, ciphered_data, password=''):
        if password == '':
            password = self.password

        salt = b'DRw\xaaj_\xfb\xca\xec\x91\xcd \xd9xk\x88\xe0\xbd\x97\xcab-\xe9\xa7D ^\xee\x93\xac\x92\x1f'
        key = PBKDF2(password, salt, dkLen=32, count=1000000)

        cipher = AES.new(key, AES.MODE_CBC)
        original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        return original_data


    # Generate the control sum
    def generate_cum(self, data):
        pass

