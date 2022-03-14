from infosec.core import assemble


def patch_program_data(program: bytes) -> bytes:
    """
    Implement this function to return the patched program. This program should
    execute lines starting with #!, and print all other lines as-is.

    Use the `assemble` module to translate assembly to bytes. For help, in the
    command line run:

        ipython3 -c 'from infosec.core import assemble; help(assemble)'

    :param data: The bytes of the source program.
    :return: The bytes of the patched program.
    """
    progArr = bytearray(program)
    patch1 = bytearray(assemble.assemble_file("./patch1.asm"))
    patch2 = bytearray(assemble.assemble_file("./patch2.asm"))

    # Add patch1 to the program's binary
    offset = 1587 # 633 in hex
    for i in range(len(patch1)):
        progArr[i+offset] = patch1[i]

    # Add patch2 to the program's binary
    offset = 1485 # 5cd in hex
    for i in range(len(patch2)):
        progArr[i+offset] = patch2[i]
    
    return bytes(progArr)


def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    patched = patch_program_data(data)
    with open(path + '.patched', 'wb') as writer:
        writer.write(patched)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <readfile-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
