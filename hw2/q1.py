class RepeatedKeyCipher:

    def __init__(self, key: bytes = bytes([0, 0, 0, 0, 0])):
        """Initializes the object with a list of integers between 0 and 255."""
        # WARNING: DON'T EDIT THIS FUNCTION!
        self.key = list(key)

    def encrypt(self, plaintext: str) -> bytes:
        """Encrypts a given plaintext string and returns the ciphertext."""
        plaintext_bytes = plaintext.encode('latin-1')
        text_length = len(plaintext)
        key_length = len(self.key)
        for i in range(text_length):
            plaintext_bytes = plaintext_bytes ^ self.key[i % key_length]
        return plaintext_bytes


    def decrypt(self, ciphertext: bytes) -> str:
        """Decrypts a given ciphertext string and returns the plaintext."""
        return self.encrypt(ciphertext).decode('latin-1')


class BreakerAssistant:

    def plaintext_score(self, plaintext: str) -> float:
        """Scores a candidate plaintext string, higher means more likely."""
        # Please don't return complex numbers, that would be just annoying.
        # TODO: IMPLEMENT THIS FUNCTION
        raise NotImplementedError()
        letters_freq = [8.2, 1.5, 2.7, 4.3, 13, 2.2, 2, 6.2, 6.9, 0.15, 0.78, 4.1, 2.5, 6.7, 7.8, 1.9, 0.096, 5.9, 6.2, 9.6, 2.7, 0.97, 2.4, 0.15, 2, 0.078]
        for i in range(len(plaintext)):
            print()


    def brute_force(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher by brute-forcing all keys."""
        # TODO: IMPLEMENT THIS FUNCTION
        raise NotImplementedError()

    def smarter_break(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher any way you like."""
        # TODO: IMPLEMENT THIS FUNCTION
        raise NotImplementedError()
