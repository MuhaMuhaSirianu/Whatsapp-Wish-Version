import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
s.connect((host 192.168.2.211,port 54956 ))

# receive data from the server
while True:
    # receive data up to 1024 bytes
    data = s.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))

# close the connection
s.close()

