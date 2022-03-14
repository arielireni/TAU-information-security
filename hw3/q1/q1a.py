def check_message(path: str) -> bool:
    """
    Return True if `msgcheck` would return 0 for the file at the specified path,
    return False otherwise.
    :param path: The file path.
    :return: True or False.
    """
    try:
        with open(path, 'rb') as reader:
            # Read data from the file, do whatever magic you need
        
            # Read the first byte, and set his value to numIterations
            byte = reader.read(1)
            numIterations = int.from_bytes(byte, "little")
            # Read the second byte, and save his value
            byte = reader.read(1)
            secondByte = int.from_bytes(byte, "little")
            # Init val a as found in the binary (0xF7)
            a = 247

            # Iterate numIterations times and xor(a, nextByte) each time
            for i in range(numIterations):
                byte = reader.read(1)
                currVal = int.from_bytes(byte, "little")
                a = a ^ currVal
        
            return secondByte == a
    except OSError:
        print("ERROR: faild to open/read ", path)

def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    if check_message(path):
        print('valid message')
        return 0
    else:
        print('invalid message')
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
