import socket

s=socket.socket()

#Port 
port = 8888

s.connect (("192.168.14.10",port))

data = s.recv(1024)

s.send(b'Hi, saya client. Terima Kasih!');

print(data)

s.close()
