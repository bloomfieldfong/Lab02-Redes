import sys
import socket
import selectors
import types
from fletcher_checksumvs2 import Algoritmo_Checksum, Error_de_checksum

sel = selectors.DefaultSelector()

def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result
def accept_wrapper(sock):
    conn, addr = sock.accept()  
    print("accepted connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  
        if recv_data:
            data.outb += recv_data
            recibido=  bytes_to_int(recv_data)
            chequeado= bytes_to_int(data.outb)
            
            error_check = Algoritmo_Checksum(recibido, chequeado)
            #algoritmo_check = Algoritmo_Checksum()
        else:
            recibido=  bytes_to_int(recv_data)
            chequeado= bytes_to_int(data.outb)
            error_check = Algoritmo_Checksum(recibido, chequeado)
            print("Por el algoritmo check_sum nos muestra que todo esta en orden",error_check)
            print("closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("echoing", repr(data.outb), "to", data.addr)
            sent = sock.send(data.outb)  
            data.outb = data.outb[sent:]


if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print("listening on", (host, port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
