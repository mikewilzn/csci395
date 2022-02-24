import socket

msg = "\r\n CSCI 395!"
endmsg = "\r\n.\r\n" 

# Set the mailserver variable to your IP running FakeSMTP
# Fill in start
mailserver =
#Fill in end 

# Create socket called clientSocket and establish a TCP connection with mailserver 
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024).decode()
print(recv) 
if recv[:3] != '220': 
    print('220 reply not received from server.') 

# Send HELO command and print server response. 
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode()) 
recv1 = clientSocket.recv(1024).decode() 
print(recv1) 
if recv1[:3] != '250': 
    print('250 reply not received from server.') 
# Send MAIL FROM command and print server response. 
from_command = 'Mail from: example@example.com\r\n'
clientSocket.send(from_command.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end 

# Send RCPT TO command and print server response. 
rcpt_command = 'RCPT TO: email@email.com\r\n'
clientSocket.send(rcptCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response. 
data = 'DATA\r\n'
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server')

# Send message data from msg variable
clientSocket.send(msg.encode()) 

# Send message end with endmsg variable
clientSocket.send(endmsg.encode())

# Send QUIT command and get server response. 
quit_command = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '221':
    print('221 reply not received from server')
    clientSocket.close()