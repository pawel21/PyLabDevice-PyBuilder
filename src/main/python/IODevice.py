import os
import signal


class BadDeviceException(Exception):
    pass


class ProblemConnectionWithDeviceException(Exception):
    pass


class IODevice:
    def __init__(self, port_to_device):
        self.device = port_to_device
        try:
            self.file_descriptor = os.open(port_to_device, os.O_RDWR)
        except Exception as e:
            raise ProblemConnectionWithDeviceException("Problem with connection: %s" %e)

    def write(self, command):
        os.write(self.file_descriptor, command)

    def read(self, length=4000):
        return os.read(self.file_descriptor, length)

    def close(self):
        os.close(self.FILE)

    def get_name(self):
        self.write("*IDN?")
        return self.read(300)

    def read_error(self):
        self.write("SYSTem:ERRor?")
        msg_error = self.read(100)
        return msg_error

    def clear_event_register(self):
        self.write("*CLS")

    def handler(self, signum, frame):
        pass