import socket

s = socket.socket(family = socket.AF_INET, type=socket.SOCK_DGRAM)
print("Berjaya buat socket")

port = 8888

s.bind(("",port))
print("Berjaya bind socket di port: " + str(port))

#s.listen(5)
print("Soket tengah menunggu client!")

while True:

	c = s.recvfrom(1024)
	msg = c[0]
	addr = c[1]
	print("Dapat capaian dari: " + str(addr))

	s.sendto(b'Terima Kasih!',addr)
	print(msg)

c.close()
