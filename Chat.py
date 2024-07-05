"""UDP Chat client/server."""
import socket
import threading
import queue
import random
import os
import time
import argparse

_SERVER_PORT = 5000


#Client Code
def ClientReceive(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(data.decode('utf-8'))
        except:
            pass


def RunClient(serverIP, clientIP):
    server = (str(serverIP), _SERVER_PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((str(clientIP), 0))
    host, port = s.getsockname()
    print('Client IP->' + str(host) + ' Port->' + str(port))
    print('Connected to Server IP->' + serverIP + ' Port->'+str(_SERVER_PORT))

    name = input('Please write your name here: ')
    if name == '':
        name = 'Guest' + str(random.randint(1000,9999))
        print('Your name is:' + name)
    print('Type qqq to quit.')
    s.sendto(name.encode('utf-8'), server)
    threading.Thread(target=ClientReceive, args=(s,)).start()
    while True:
        data = input()
        if data == 'qqq':
            break
        if data=='':
            continue
        data = '['+name+']' + '->'+ data
        s.sendto(data.encode('utf-8'),server)
    s.sendto(data.encode('utf-8'),server)
    s.close()
    os._exit(1)
#Client Code Ends Here


#Server Code
def ServerReceive(sock, recvPackets):
    while True:
        data, addr = sock.recvfrom(1024)
        recvPackets.put((data, addr))

def RunServer(host):
    port = _SERVER_PORT
    print('Server hosting on IP->' + str(host) + ' Port->' + str(port))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    clients = set()
    recvPackets = queue.Queue()

    print('Server Running...')

    threading.Thread(target=ServerReceive, args=(s, recvPackets)).start()

    while True:
        if not recvPackets.empty():
            data, addr = recvPackets.get()
            if addr not in clients:
                clients.add(addr)
                continue
            data = data.decode('utf-8')
            if data.endswith('qqq'):
                clients.remove(addr)
                continue
            print(str(addr)+data)
            for c in clients:
                if c!=addr:
                    s.sendto(data.encode('utf-8'), c)
        else:
            time.sleep(.05)
    s.close()
#Serevr Code Ends Here


def main():
    parser = argparse.ArgumentParser(
        prog='Chat.py',
        description='Simple chat client / server.')
    parser.add_argument('-s', '--server', type=str, required=False, nargs='?', const=socket.gethostbyname(socket.gethostname()), help='IP address of the server when running as a server, otherwise, the server IP to connect to when running as a client.')
    parser.add_argument('-c', '--client', type=str, required=False, nargs='?', const=socket.gethostbyname(socket.gethostname()), help='IP address of the client.')

    args = parser.parse_args()

    server = args.server
    if server is None:
        server = socket.gethostbyname(socket.gethostname())

    if args.client is not None:
        RunClient(server, args.client)
    else:
        RunServer(server)


if __name__ == '__main__':
    main()