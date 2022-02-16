import socket

host = input("Enter website: ")

port = int(input("Enter port: "))


sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

if(sock.connect_ex((host, port)) == 0):
    state = "open"
else:
    state = "closed"

sock.close()

print("Port", port, "is", state, "on host", host)
