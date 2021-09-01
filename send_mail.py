import socket

server_info = ("192.168.10.45", 25)

socket = socket.socket()
socket.connect(server_info)

def send_message(data):
    arr = bytes(data, 'utf-8')
    socket.send(arr)

username = input("Enter your username: ")
password = input("Enter your password: ")
recipient = input("Recipient: ")
data = input("Your message: ")
auth = username + "" + password
#auth = auth.encode("base64").replace("\n", "")
send_message("HELO\r\n")
print ("EHLO Response: " + str(socket.recv(1024)))
#socket.send("AUTH PLAIN "+auth+"\r\n")
#print ("AUTH Response: " + socket.recv(1024))
#socket.send("MAIL FROM:<"+username+">\r\n")
send_message("MAIL FROM:<"+username+">\r\n")
print ("MAIL FROM Response: " + str(socket.recv(1024)))
send_message("RCPT TO:"+recipient+"\r\n")
#socket.send("RCPT TO:"+recipient+"\r\n")
print ("RCPT TO Response: " + str(socket.recv(1024)))
send_message("RCPT TO:"+recipient+"\r\n")
#socket.send("RCPT TO:"+recipient+"\r\n")
print ("RCPT TO Response: " + str(socket.recv(1024)))
#socket.send("DATA\r\n")
send_message("DATA\r\n")
print ("DATA Response: " + str(socket.recv(1024)))
#socket.send(data + "\r\n.\r\n")
send_message(data + "\r\n.\r\n")
print ("RAW DATA Response: " + str(socket.recv(1024)))
#socket.send("QUIT\r\n")
send_message("QUIT\r\n")
print ("QUIT Response: " + str(socket.recv(1024)))
print ("Done.")

socket.close()

