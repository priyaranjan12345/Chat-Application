from socket import *
from _thread import *

s = socket(AF_INET, SOCK_STREAM)

ip = '127.0.0.1'
port = 1123
#myip = s.gethostname()

name = input("Enter Your Name :")

s.connect((ip, port))

def recvMsg(s):
    while True:
        data = s.recv(1024).decode("utf-8")
        if data:
            print('\n',data)
        else:
            continue

while True:
    start_new_thread(recvMsg, (s, ))
    txt = input("\nEnter Message:")
    if not txt:
        continue
    else:
        msg = '%s : %s' %(name, txt)
        
    s.send(msg.encode("utf-8"))
    


s.close()
