# Thanks for the writer of this function
# https://blog.csdn.net/QQ_1993445592/article/details/102578595
import base64

from Crypto.Cipher import AES

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def encrypt(key, data):
    """
    AES Encrypt
    :param key: Key
    :param data: Original text
    :return: Ciphertext
    """
    data = pad(data)
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.encrypt(data.encode())
    encodestrs = base64.b64encode(result)
    enctext = encodestrs.decode('utf8')
    print(enctext)
    return enctext


def decrypt(key, data):
    """
    AES Decrypt
    :param key: Key
    :param data: Original text
    :return: Ciphertext
    """
    data = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_ECB)
    text_decrypted = unpad(cipher.decrypt(data))
    text_decrypted = text_decrypted.decode('utf8')
    print(text_decrypted)
    return text_decrypted
