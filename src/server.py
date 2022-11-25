import socket

host = '127.0.0.1'
port = 55554

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((host, port))
            clients = []
            print('Start Server')
            while True:
                data, address = sock.recvfrom(1024)
                print(data.decode('utf-8'))
                if address not in clients:
                    clients.append(address)
                for client in clients:
                    if client == address:
                        continue
                    try:
                        sock.sendto(data, client)
                    except:
                        clients.remove(client)
        finally:
            print("Close server")
            sock.close()
