import socket

s = socket.socket()
host = socket.gethostname()
port = 12345 ##fill in later with proper port channel
##possibly have this as user input when first running server software
##possibly write feature to scan for open ports and give a list to user to pick from
s.bind(host,port)

s.listen(5)## 5 connections for now will test later to see if more or less is required
##also this is just to get a conneciton started will have to figure out how to make
##multiple connections occur at the same time
while True:
    c, addr = s.accept()
    print 'Got connection from: ', addr
    c.send('You have connected to RaspIRCS please wait for instructions.')
    c.close()
