import socket, sys, select
def client():
    s = socket.socket()
    ip = socket.gethostname()
    port = 9009
    try:
        s.connect((ip, port))
        print "Connected!"
    except:
        print "Host not found! Goodbye!"
    while True:
        socket_list = [sys.stdin, s]
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print "Whoops! Something went wrong!"
                    sys.exit()
                else:
                    sys.stdout.write(msg)
                    sys.stdout.write('<You> '); sys.stdout.flush()
            else:
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('<You> '); sys.stdout.flush()
if __name__ == "__main__":
    sys.exit(client())
