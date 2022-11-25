import socket
import threading

host = '127.0.0.1'
port = 55554


def read_sok():
    while 1:
        data = sock.recv(1024)
        print(data.decode('utf-8'))


if __name__ == '__main__':
    server = host, port
    print('Введите свой ник: ', end='')
    alias = input()
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', 0))
        sock.sendto((alias + ' Присоединился к нашему чату').encode('utf-8'), server)
        thread = threading.Thread(target=read_sok)
        thread.start()
        while True:
            message = input()
            sock.sendto((alias + ': ' + message).encode('utf-8'), server)
