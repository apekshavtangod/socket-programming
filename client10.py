import socket

def send_request(username, password):
    """Send the authentication request to the server."""
    try:
        # Create a socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 8080))
        
        # Send the username and password as a space-separated string
        request = f"{username} {password}"
        client_socket.sendall(request.encode())

        # Receive the authentication result from the server
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")

        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Prompt user for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    send_request(username, password)
