import socket
import signal
import sys


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50006              # Arbitrary non-privileged port


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connected by', addr
while 1:
  data = conn.recv(1024)
  if not data: break
  print(data)
  #conn.sendall(data)
  if(data == "exit"):
      break
conn.close()
s.close()
