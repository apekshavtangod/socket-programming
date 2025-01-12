import socket

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    if request.startswith("UPLOAD"):
        filename = request.split()[1]
        with open(f"server_{filename}", "wb") as f:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                f.write(data)
        print(f"File {filename} uploaded successfully.")
    
    elif request.startswith("DOWNLOAD"):
        filename = request.split()[1]
        try:
            with open(filename, "rb") as f:
                client_socket.send(f.read())
            print(f"File {filename} sent successfully.")
        except FileNotFoundError:
            client_socket.send(b"File not found")
    
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(5)
    print("Server is listening on port 12345...")

    while True:
        client_socket, _ = server.accept()
        handle_client(client_socket)

if __name__ == "__main__":
    main()
