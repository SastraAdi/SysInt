import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connected: {client_address}")

    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode()

        if not message:
            print(f"Disconnected: {client_address}")
            break

        print(f"Received from {client_address}: {message}")

        # Broadcast message to all clients
        broadcast(message)

    client_socket.close()

# Function to broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.send(message.encode())

# Server configuration
HOST = '127.0.0.1'  # localhost
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)  # Max number of connections

print(f"Server listening on {HOST}:{PORT}")

clients = []

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)

    # Create a new thread for each client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
