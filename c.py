from socket import *

host = gethostname()
port = 55551
print(host)
cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host,port))

while 1:
    msg = input("Digite: ")
    print(type(msg))
    cli.send(msg.encode())