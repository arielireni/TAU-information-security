import string

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
        letters_map = self.get_frequency_letters_map()
        freq_score = 0.0
        for i in range(len(str)):
            unicode_char = ord(str[i])
            if(unicode_char < 0 or unicode_char > 127):
                return -1
            if(unicode_char >= 97 and unicode_char <= 122):
                freq_score += letters_map[str[i]]
        # normalize the score
        score = (len(str) - freq_score) / len(str)
        return score

    
    def get_frequency_letters_map() -> dict:
        # Based on data from https://en.wikipedia.org/wiki/Letter_frequency
        return {
            'a': 8.2, 
            'b': 1.5,
            'c': 2.7,
            'd': 4.3,
            'e': 13, 
            'f': 2.2,
            'g': 2,
            'h': 6.2,
            'i': 6.9, 
            'j': 0.15,
            'k': 0.78,
            'l': 4.1,
            'm': 2.5,
            'n': 6.7,
            'o': 7.8,
            'p': 1.9, 
            'q': 0.096, 
            'r': 5.9,
            's': 6.2,
            't': 9.6,
            'u': 2.7,
            'v': 0.97,
            'w': 2.4, 
            'x': 0.15,
            'y': 2,
            'z': 0.078
        }


    def brute_force(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher by brute-forcing all keys."""
        # for each index in the key
        key = [0 for i in range(key_length)]
        max_score = 0
        max_str = ''
        for i in range(key_length):
            for j in range(2**8 + 1):
                key[i] = j
                bytes_key = bytes(key)
                str_key = bytes_key.decode('latin-1')
                curr_score = self.plaintext_score(str_key)
                if curr_score > max_score:
                    max_score = curr_score
                    max_str = str_key
        return max_str


    def smarter_break(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher any way you like."""
        # TODO: IMPLEMENT THIS FUNCTION
        raise NotImplementedError()
