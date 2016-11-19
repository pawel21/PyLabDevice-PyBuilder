import unittest

from device.IODevice import IODevice, ProblemConnectionWithDeviceException
from mock import patch


class IODeviceTest(unittest.TestCase):
    @patch("os.open")
    def test_should_raise_exception(self, os_open_mock):
        # GIVEN
        os_open_mock.side_effect = ProblemConnectionWithDeviceException("not existing path")
        fake_port_to_device = "foo"
        # WHEN & THEN
        with self.assertRaisesRegexp(ProblemConnectionWithDeviceException, "Problem with connection: not existing path"):
            IODevice(fake_port_to_device)
