import socket
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives import padding

# NOTE: I used this resource as a reference - https://gist.github.com/dennislwy/65767fdce205b2811586beb054571b30 and also - https://www.programcreek.com/python/example/96021/cryptography.hazmat.primitives.padding.PKCS7

key = 'your key 32bytesyour key 32bytes'
iv = '1234567812345678' # 16 bytes initialization vector

def receive_message(port: int) -> str:
    """Receive *encrypted* messages on the given TCP port.

    As Winston sends encrypted messages, re-implement this function so to
    be able to decrypt the messages.

    Notes:
    1. The encryption is based on AES.
    2. Julia and Winston already have a common shared key, just define it on your own.
    3. Mind the padding! AES works in blocks of 16 bytes.
    """
    listener = socket.socket()
    try:
        listener.bind(('', port))
        listener.listen(1)
        connection, address = listener.accept()
        try:
            ciphertext = b64decode(connection.recv(1024).decode("latin-1"))
            aes = AES.new(key.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))
            padded_data = aes.decrypt(ciphertext)
            
            # remove padding 
            unpadder = padding.PKCS7(128).unpadder()
            output = unpadder.update(padded_data) + unpadder.finalize()

            return output.decode('latin-1')

        finally:
            connection.close()
    finally:
        listener.close()


def main():
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    message = receive_message(1984)
    print('received: %s' % message)


if __name__ == '__main__':
    main()
