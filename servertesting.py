#from graphics import *
import socket, sys, select
socks = []
s = socket.socket()
def server():
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ip = raw_input("IP> ")
    port = 9009
    s.bind((ip, port))
    s.listen((5))
    socks.append(s)
    while True:
        ready_to_read,ready_to_write,in_error = select.select(socks,[],[],0)
        for sock in ready_to_read:
            if sock == s:
                sockx, addr = s.accept()
                socks.append(sockx)
                broadcast(s, sockx, "<%s:%s> joined the chat\n" % addr)
            else:
                try:
                    msg = sock.recv(4096)
                    if msg:
                        broadcast(s, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + msg)
                    else:
                        if sock in socks:
                            socks.remove(sock)
                        broadcast(s, sock, "Client (%s, %s) is offline\n" % addr)
                except:
                    broadcast(s, sock, "Client (%s, %s) is offline\n" % addr)
                    continue
def broadcast (server_socket, sock, message):
    for socket in socks:
        # send the message only to peer
        if socket != s and socket != sock :
            try :
                socket.send(msg)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in socks:
                    socks.remove(socket)
    #w = GraphWin('inventory', 2000, 1000)
    #words = Text(Point(w.getWidth()/2, 20), '%s' % messgae)
    #inv.draw(w)
    #w.getMouse()
    #w.close()
server()
