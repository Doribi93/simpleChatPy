import threading
import socket

local_host = '127.0.0.1'
port = 9001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((local_host, port))
server.listen()

user_lists = []
username_lists = []

def juggle(client):
    while True:
        try:
            messages = client.recv(1024)
            muster(messages)
        except:
            index = user_lists.index(client)
            user_lists.remove(client)
            user_lists.close()
            username = username_lists[index]
            muster(f'{username} has left the server.'.encode('utf-8'))
            username_lists.remove(username)
            break

def muster(messages):
    for client in user_lists:
        client.send(messages)

def get():
    while True:
        print('.:[CONNECTION ESTABLISHED]:.\n')
        client, address = server.accept()
        print(f'STATUS: ONLINE, CONNECTED TO {str(address)}')
        client.send('Name?'.encode('utf-8'))
        username = client.recv(1024)
        username_lists.append(username)
        user_lists.append(client)
        print(f'{username} is connected.'.encode('utf-8'))
        muster(f'\n{username} has entered the server.'.encode('utf-8'))
        client.send('Welcome to Default Server!\n'.encode('utf-8'))
        
        thread = threading.Thread(target = juggle, args = (client, ))
        thread.start()
        
if __name__ == "__main__":
    get()