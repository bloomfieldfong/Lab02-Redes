import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()
#messages = [b"Hola Michi.", b"que tal estas."]
#messages = [b"Hola Michi que tal estas"]
#mensaje= "hola pascalito"
#mensaje= mensaje.encode("ascii", "ignore")
mensaje= input(str(">>"))
mensaje = ascii(mensaje)
#mensaje = mensaje.encode("ascii", "ignore")
x = bytes(mensaje, 'ASCII')
print("x", x)
messages = [x]
print(messages)

def viterbi_segment(text):
    n = len(text)
    words = [''] + list(text)
    best = [1.0] + [0.0] * n

    for i in range(n+1):
        for j in range(0, i):
            w = text[j:i]
            if P[w] * best[i - len(w)] >= best[i]:
                best[i] = P[w] * best[i - len(w)]
                words[i] = w
                sequence = []; i = len(words)-1
                while i > 0:
                    sequence[0:0] = [words[i]]
                    i = i - len(words[i])

        return sequence, best[-1]

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print("Empezando conexion", connid, "a", server_addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid=connid,
            msg_total=sum(len(m) for m in messages),
            recv_total=0,
            messages=list(messages),
            outb=b"",
        )
        sel.register(sock, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  
        if recv_data:
            print("Recibido", repr(recv_data), "fue recibida por:", data.connid)
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print("Cerrando conexion", data.connid)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
        if data.outb:
            print("Enviando", repr(data.outb), "a la conexion", data.connid)
            sent = sock.send(data.outb)  
            data.outb = data.outb[sent:]


if len(sys.argv) != 4:
    print("Ruta:", sys.argv[0], "<host> <port> <num_connections>")
    sys.exit(1)
host, port, num_conns = sys.argv[1:4]
start_connections(host, int(port), int(num_conns))

try:
    while True:
        events = sel.select(timeout=1)
        if events:
            for key, mask in events:
                service_connection(key, mask)
                
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
