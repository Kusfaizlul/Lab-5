import socket
import touch
from Crypto.Cipher import AES

def encrypt(encrypt_data):
        obj = AES.new(b"1122334456789001" , AES.MODE_CFB, b"2299225510784791")
        data = obj.encrypt(encrypt_data)
        return data

def decrypt(decrypt_data):
        obj = AES.new(b"1122334456789001" , AES.MODE_CFB, b"2299225510784791")
        data = obj.decrypt(decrypt_data)
        return data


s = socket.socket()

PORT = 9898

print("\n Server is listing on port :", PORT, "\n")

s.bind(('', PORT))

s.listen(10)


while True:
    conn, addr = s.accept()
    print ("\n Connection is Accepted from the Client !! ")

    ClientFile = conn.recv(1024)
    print ("\n Before Decryption : " + str(ClientFile))
    decrypted = decrypt(ClientFile)
    ClientFile = decrypted.decode()
    print ("\n After Decryption with decode : " + str(ClientFile))

    touch.touch(ClientFile)
    file = open(ClientFile,"wb")

    msg = "\n\n |-----------------------------------|\n  Hi Client[IP address: "+ addr[0] + "], \n  ֲֳ**Welcome to Server** \n  - You can put Your Trust On Us !! \n |-----------------------------------|\n \n\n"

    encrypted = encrypt(msg.encode())
    conn.send(encrypted)

    RecvData = conn.recv(1024)
    temp = decrypt(RecvData)

    while RecvData:
        file.write(temp)

        RecvData = conn.recv(1024)
        temp = decrypt(RecvData)

    file.close()
    print("\n File has been copied and stored successfully !! ")

    conn.close()
    print("\n Server closed the connection \n \n")

    break
