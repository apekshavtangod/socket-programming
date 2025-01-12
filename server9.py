import socket

def handle_request(client_socket):
    try:
        request = client_socket.recv(1024).decode()
        if request:
            print(f"Request received:\n{request}")
            
            # Extract the requested file name from the GET request
            lines = request.splitlines()
            request_line = lines[0]
            file_name = request_line.split()[1]
            
            if file_name == '/':
                file_name = '/index.html'  # Default file if no specific file is requested
            
            try:
                # Open the requested file (e.g., index.html) and send it back
                with open(file_name[1:], 'rb') as f:
                    content = f.read()
                    response = 'HTTP/1.1 200 OK\r\n'
                    response += 'Content-Type: text/html\r\n\r\n'
                    client_socket.sendall(response.encode())
                    client_socket.sendall(content)
            except FileNotFoundError:
                # If file is not found, return 404 error
                response = 'HTTP/1.1 404 Not Found\r\n'
                response += 'Content-Type: text/html\r\n\r\n'
                response += '<html><body><h1>404 Not Found</h1></body></html>'
                client_socket.sendall(response.encode())
        else:
            print("No request received.")
    except Exception as e:
        print(f"Error handling request: {e}")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))  # Binding to localhost and port 8080
    server_socket.listen(5)
    print("HTTP Server listening on http://localhost:8080 ...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        handle_request(client_socket)

if __name__ == "__main__":
    start_server()
