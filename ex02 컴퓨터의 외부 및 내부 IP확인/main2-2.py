import socket

#? AF_INET: IPv4, socket.SOCK_STREAM: TCP IP
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.com", 443))
print(in_addr.getsockname()[0])