import socket

# Predefined credentials (username: password)
USER_CREDENTIALS = {
    "user1": "password1",
    "user2": "password2",
    "admin": "admin123"
}

def authenticate(username, password):
    """Authenticate the user by checking against predefined credentials."""
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        return "Authentication successful!"
    else:
        return "Authentication failed. Invalid username or password."

def handle_client(client_socket):
    """Handle the client's request and authenticate."""
    try:
        # Receive the authentication request from the client
        request = client_socket.recv(1024).decode()
        print(f"Received request: {request}")
        
        # Split the received request into username and password
        username, password = request.split(" ")

        # Authenticate the user
        result = authenticate(username, password)
        
        # Send authentication result back to the client
        client_socket.send(result.encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def start_server():
    """Start the authentication server to handle client requests."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))  # Binding to localhost and port 8080
    server_socket.listen(5)
    print("Authentication server started on port 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
