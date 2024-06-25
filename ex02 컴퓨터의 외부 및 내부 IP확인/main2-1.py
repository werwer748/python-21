import socket

in_addr = socket.gethostbyname(socket.gethostname())

print(in_addr) # 공유기에서 할당해준 내부IP