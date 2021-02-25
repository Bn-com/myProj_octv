# -*- coding: utf-8 -*-
__author__ = 'huangzhongwei'

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('', 8271))
#s.sendto(u'{"cmd" : "restart"}', ('192.168.0.255', 8271))
s.sendto(u'{"cmd" : "box"}', ('192.168.2.215', 8271))
#s.sendto(u'{"cmd" : "shutdown"}', ('192.168.2.255', 8271))
s.close()