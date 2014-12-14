#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Alienpuke - That's how it looks if an alien.. just start it and you will see..
"""

__author__ = 'XeN'
__copyright__ = 'Copyright 2014, XeN'
__credits__ = ['lacce']
__license__ = 'MIT'
__version__ = '1.0.0'
__maintainer__ = 'XeN'
__email__ = 'xen@c-base.org'
__status__ = 'Production'

import sys
import random
import socket
import colorsys

WIDTH = 16
HEIGHT = 40
MATELIGHT_HOST = 'matelight.cbrp3.c-base.org'
MATELIGHT_PORT = 1337


def update(matrix):
    data = []
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            for val in colorsys.hsv_to_rgb(matrix[x][y], 1, 1):
                data.append(int(val * 255))
    data_as_bytes = bytearray(data)
    data_as_bytes + bytearray([0, 0, 0, 0])
    #sock.sendto(data_as_bytes, ('matelight.cbrp3.c-base.org', 1337))
    sock.sendto(data_as_bytes, (MATELIGHT_HOST, MATELIGHT_PORT))


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    puke = [[0 for _ in range(HEIGHT)] for _ in range(WIDTH)]
    speeds = [[random.random() / 10000 + 0.001 for _ in range(HEIGHT)] for _ in range(HEIGHT)]
    
    while True:
        try:
            update(puke)
            for x in range(WIDTH):
                for y in range(HEIGHT):
                    puke[x][y] = puke[x][y] + speeds[x][y] % 1
        except KeyboardInterrupt:
            sys.exit(0)
