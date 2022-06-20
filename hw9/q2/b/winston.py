import socket
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives import padding

# NOTE: I used this resource as a reference - https://gist.github.com/dennislwy/65767fdce205b2811586beb054571b30 and also - https://www.programcreek.com/python/example/96021/cryptography.hazmat.primitives.padding.PKCS7

plaintext = b'I love you'
key = 'your key 32bytesyour key 32bytes'
iv = '1234567812345678' # 16 bytes initialization vector

def send_message(ip: str, port: int):
    """Send an *encrypted* message to the given ip + port.

    Julia expects the message to be encrypted, so re-implement this function accordingly.

    Notes:
    1. The encryption is based on AES.
    2. Julia and Winston already have a common shared key, just define it on your own.
    3. Mind the padding! AES works in blocks of 16 bytes.
    """
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    aes = AES.new(key.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))
    ciphertext = aes.encrypt(padded_data)

    connection = socket.socket()
    try:
        connection.connect((ip, port))
        connection.send(b64encode(ciphertext))
    finally:
        connection.close()


def main():
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    send_message('127.0.0.1', 1984)


if __name__ == '__main__':
    main()
