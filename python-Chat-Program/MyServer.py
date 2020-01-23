from socket import *
from thread import *

fo = open("MyServerHistory.txt","a")
s = socket(AF_INET, SOCK_STREAM)

ip = '127.0.0.1'
port = 1123

s.bind((ip, port))
print 'server is Stared at:',ip,':',port

s.listen(8)

users = []
addres = []
msg = ''
d=''

def Server(c, addr, users, addres):
    while True:
        msg = c.recv(1024).decode("utf-8")
        print addr,':',msg
        #-------files write---------
        d = str(addr)
        fo.write('\n')
        fo.write(d)
        fo.write(':')
        fo.write(msg)
        fo.write('\n')
        #---------------------------
        if msg:
            users.remove(c)# remove the sender
            for i in users:
                i.send(msg.encode("utf-8"))
            users.append(c)# again add the sender

while True:
    try:
        conn, addr = s.accept()
        users.append(conn)
        addres.append(addr)
    
        start_new_thread(Server, (conn, addr, users, addres))
    
        print 'New connection: ',addr
    except Exception as e:
        print 'Error: {e}'
fo.close()
s.close()
conn.close()
