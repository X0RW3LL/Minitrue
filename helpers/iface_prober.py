#!/usr/bin/env python3

import socket
import fcntl
import struct
import sys
import os

def ip_addr(ifname):
    """
    Returns interface IPv4 address

    :param ifname: Interface name whose IPv4 address is to be retrieved
    :type ifname: str
    :return: Interface IPv4 address
    """
    # Credit: https://stackoverflow.com/a/24196955
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        addr = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                            ifname[:15].encode('latin-1')))[20:24])
        return addr
    except OSError:
        pass

def get_interfaces():
    """
    Queries interface names and addresses

    :return: "interface_name [interface_IPv4]"
    """
    interfaces = []
    interface_list = os.listdir('/sys/class/net/')
    for iface in interface_list:
        if ip_addr(iface):
            interfaces.append("{} [{}]".format(iface, ip_addr(iface)))
    return interfaces
