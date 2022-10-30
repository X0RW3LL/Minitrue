#!/usr/bin/env python3

import socket, fcntl, struct, sys, os


def ip_addr(ifname):
    # Credit: https://stackoverflow.com/a/24196955
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        addr = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', 
                                            ifname[:15].encode('latin-1')))[20:24])
        return addr
    except OSError:
        pass

def get_interfaces():
    '''
    Gets interface names and addresses
    
    Returns:
    interfaces (str): <interface> [<IP>]
    '''
    interfaces = []
    interface_list = os.listdir('/sys/class/net/')
    for iface in interface_list:
        if ip_addr(iface):
            interfaces.append("{} [{}]".format(iface, ip_addr(iface)))
    return interfaces
