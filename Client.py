import socket
import threading

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except OSError:  # Client has left
            break

# Client configuration
HOST = '127.0.0.1'  # localhost
PORT = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    # Send message to the server
    message = input()
    client_socket.send(message.encode())

client_socket.close()
