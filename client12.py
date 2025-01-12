import socket

def send_data_and_check_parity(data):
    """Send the data to the server and receive the response."""
    try:
        # Create a socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 8080))  # Connecting to the server on port 8080

        # Send the binary data to the server
        client_socket.sendall(data.encode())

        # Receive the server's response
        response = client_socket.recv(1024).decode()
        print(f"Server Response: {response}")
        
        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    data = input("Enter a binary string to check parity: ")
    send_data_and_check_parity(data)
