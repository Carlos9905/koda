# -*- coding: utf-8 -*-
# Koda

import serial.tools.list_ports

from koda.addons.hw_drivers.interface import Interface


class SerialInterface(Interface):
    connection_type = 'serial'

    def get_devices(self):
        serial_devices = {}
        for port in serial.tools.list_ports.comports():
            serial_devices[port.device] = {
                'identifier': port.device
            }
        return serial_devices
