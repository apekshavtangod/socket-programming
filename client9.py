import socket

def send_request():
    try:
        # Create a socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 8080))

        # Send a basic GET request to the server
        request = "GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"
        client_socket.sendall(request.encode())

        # Receive and print the server's response
        response = client_socket.recv(1024).decode()
        print("Response from server:\n")
        print(response)
        
        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_request()
