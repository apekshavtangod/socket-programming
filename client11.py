import socket

def request_ip_and_mac():
    """Request the IP and MAC addresses from the server."""
    try:
        # Create a socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 8080))  # Connecting to the server on port 8080
        
        # Receive the response from the server
        response = client_socket.recv(1024).decode()
        print(f"Server Response:\n{response}")
        
        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    request_ip_and_mac()
