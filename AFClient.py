import socket                   # Import socket module
import time
import sys

i=0

fp = open('clog.txt', 'a')            # Create a socket object     # Get local machine name
s = socket.socket()
port = 60000                    # Reserve a port for your service.
s.bind(('10.100.0.6', 60001))
s.connect(('10.100.0.5', 60001))

#except :
#    s.close()
#    execfile('client2.py')
#    sys.exit()
fp.write("1: ")
fp.write(str(int(time.time() * 1000000)))
fp.write('\n')
s.send("Server 6:  Hello server 5!")
s.close()

