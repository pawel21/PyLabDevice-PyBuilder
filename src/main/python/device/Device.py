import fnmatch
import os
from IODevice import IODevice


class Device:
    _PATH_TO_DEV_DIR = "/dev"
    map_device = {}
    available_port = ["/dev/usbtmc0", "/dev/usbtmc1"]

    def available_device(self):
        list_of_path_usb_device = self._create_list_of_usb_device()
        for path_usb_device in list_of_path_usb_device:
            self.map_device[path_usb_device] = (IODevice(path_usb_device).get_name())
        return self.map_device

    @staticmethod
    def connect_with_device(port_to_device):
        device = IODevice(port_to_device)
        return device

    def _create_list_of_usb_device(self):
        list_of_device = os.listdir(self._PATH_TO_DEV_DIR)
        list_of_path_usb_device = []
        for device in list_of_device:
            if fnmatch.fnmatch(device, 'usb*'):
                list_of_path_usb_device.append(os.path.join(self._PATH_TO_DEV_DIR, device))
        return list_of_path_usb_device

