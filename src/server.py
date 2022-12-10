import socket
import threading

host = '127.0.0.1'
port = 55555


def send_message(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            send_message(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicks[index]
            send_message('{} left!'.format(nickname).encode('ascii'))
            nicks.remove(nickname)
            break


def main():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nick = client.recv(1024).decode('ascii')
        nicks.append(nick)
        clients.append(client)

        print("Nickname is {}".format(nick))
        send_message("{} joined!".format(nick).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    clients = []
    nicks = []
    main()
