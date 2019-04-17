import subprocess
import socket

HOST=''
PORT=50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = s.connect_ex((HOST,PORT))


if result == 0:
   print ("Port on another computer is open. Running Client Program.")
   subprocess.call(['python','client.py'])
else:
   print ("Port on another computer is not open. Running Server Program.")
   subprocess.call(['python','server.py'])
