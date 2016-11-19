import struct


class ConvertData:
    @staticmethod
    def convert_float_to_hex(data):
        return hex(struct.unpack('<Q', struct.pack('<d', data))[0])