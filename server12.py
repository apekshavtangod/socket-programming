import socket

def check_even_parity(data):
    """Check if the given binary string has even parity."""
    ones_count = data.count('1')
    return ones_count % 2 == 0  

def handle_client(client_socket):
    """Handle the connection with the client."""
    data = client_socket.recv(1024).decode()
    if check_even_parity(data):
        response = "Even parity"
    else:
        response = "Odd parity"
    
    client_socket.send(response.encode())
    client_socket.close()

def start_server():
    """Start the TCP server and listen for connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))  
    server_socket.listen(5)
    print("Server is listening on port 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with: {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
