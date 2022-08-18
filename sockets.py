#!/usr/bin/python3

from pydoc import cli
import socket
import os
from urllib import response

target_host = "site"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
payload = "GET / HTTP/1.1\r\nHost: site\r\nConnection: keep-alive\n\r\n"
client.send(payload.encode(encoding='utf-8'))

while True:
    response = client.recv(2048)
    print(response.decode('utf-8'))

