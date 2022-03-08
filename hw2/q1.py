class RepeatedKeyCipher:

    def __init__(self, key: bytes = bytes([0, 0, 0, 0, 0])):
        """Initializes the object with a list of integers between 0 and 255."""
        # WARNING: DON'T EDIT THIS FUNCTION!
        self.key = list(key)

    def encrypt(self, plaintext: str) -> bytes:
        """Encrypts a given plaintext string and returns the ciphertext."""
        plaintext_bytes = bytearray(plaintext.encode('latin-1'))
        key_length = len(self.key)
        bytes_arr = []
        byte_count = 0
        # XOR byte by byte
        for byte in plaintext_bytes:
            bytes_arr.append(byte ^ self.key[byte_count % key_length])
            byte_count += 1
            
        return bytes(bytearray(bytes_arr))

    def decrypt(self, ciphertext: bytes) -> str:
        """Decrypts a given ciphertext string and returns the plaintext."""
        return self.encrypt(ciphertext.decode('latin-1')).decode('latin-1')


class BreakerAssistant:

    def plaintext_score(self, plaintext: str) -> float:
        """Scores a candidate plaintext string, higher means more likely."""
        # Please don't return complex numbers, that would be just annoying.
        letters_map = self.get_frequency_letters_map()
        repetitions_map = self.get_repetitions_map(plaintext)
        total_score = 0.0
        length = len(plaintext)
        for i in range(length):
            unicode_char = ord(plaintext[i])
            if(unicode_char < 0 or unicode_char > 127):
                return -1
            if(unicode_char >= 97 and unicode_char <= 122):
                freq_score = letters_map[plaintext[i]]
                 # normalize the score
                rep = repetitions_map[plaintext[i]]
                total_score += (freq_score * ((length - rep)/length)) 
        return total_score

    # Returns the map of english letters and their frequencies
    def get_frequency_letters_map(self) -> dict:
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
    
    # Returns the number of repetitions of each char in the string
    def get_repetitions_map(self, plaintext: str) -> dict:
        rep_map = dict()
        for char in plaintext:
            if char in rep_map:
                rep_map[char] += 1
            else:
                rep_map[char] = 1
            
        return rep_map


    def brute_force(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher by brute-forcing all keys."""
        max_score = -1
        max_plaintext = ''
        for key_int in range(2**(8*key_length)):
            # convert key_int to array of bytes from https://www.geeksforgeeks.org/how-to-convert-int-to-bytes-in-python/
            key = key_int.to_bytes(key_length, byteorder='little')
            curr_cipher = RepeatedKeyCipher(key)
            # Decrypt and save the score for cipher_text with the current key
            curr_plaintext = curr_cipher.decrypt(cipher_text)
            curr_score = self.plaintext_score(curr_plaintext)
            if curr_score > max_score:
                max_score = curr_score
                max_plaintext = curr_plaintext 
        return max_plaintext
 

    def smarter_break(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher any way you like."""
        max_keys = []
        for i in range(key_length):
            max_score = -1
            max_key = 0
            # Key for each time seperately and therefore there are only 2**8 options 
            for j in range(2 ** 8):
                key = j.to_bytes(1, byteorder='little')
                curr_cipher = RepeatedKeyCipher(key)
                i_cipher_text = []
                index = 0
                for byte in cipher_text:
                    if index % key_length == i:
                        i_cipher_text.append(byte)
                    index += 1
                i_cipher_text = bytes(i_cipher_text)

                curr_plaintext = curr_cipher.decrypt(i_cipher_text)
                curr_score = self.plaintext_score(curr_plaintext)
                if curr_score > max_score:
                    max_score = curr_score
                    max_key = j
            max_keys.append(max_key)
        
        final_key = bytes(bytearray(max_keys))        
        final_cipher = RepeatedKeyCipher(final_key)
        final_plaintext = final_cipher.decrypt(cipher_text)
        return final_plaintext



