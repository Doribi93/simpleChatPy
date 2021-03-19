import threading
import socket

print("====================================")
print("||       SIMPLE CHAT v0.001       ||")
print("====================================")
usr_name = input('Enter a username: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9001))

def client_receive():
    while True:
        messages = client.recv(1024).decode('utf-8')
        
        if messages == "Name?":
            client.send(usr_name.encode('utf-8'))
        else:
            print(messages)

def client_send():
    while True:
        messages = f'{usr_name} : {input("")}'
        client.send(messages.encode('utf-8'))

receiving_thread = threading.Thread(target = client_receive)
receiving_thread.start()
sending_thread = threading.Thread(target = client_send)
sending_thread.start()