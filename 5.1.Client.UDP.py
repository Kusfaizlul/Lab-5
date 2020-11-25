import socket

s = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

ServerAdd = ("192.168.14.10", 8888)

s.sendto(b"Hi, saya client. Terima Kasih!", ServerAdd);

data = s.recvfrom(1024)

print(data[0])

s.close()
