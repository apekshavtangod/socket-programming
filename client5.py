import socket
import os

def upload_file(client_socket, filename):
    client_socket.send(f"UPLOAD {filename}".encode())
    with open(filename, "rb") as f:
        while (chunk := f.read(1024)):
            client_socket.send(chunk)
    print(f"File {filename} uploaded successfully.")

def download_file(client_socket, filename):
    client_socket.send(f"DOWNLOAD {filename}".encode())
    data = client_socket.recv(1024)
    if data == b"File not found":
        print("Error: File not found on server.")
    else:
        with open(f"downloaded_{filename}", "wb") as f:
            f.write(data)
        print(f"File {filename} downloaded successfully.")

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    while True:
        print("1. Upload a file")
        print("2. Download a file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the filename to upload: ")
            if os.path.exists(filename):
                upload_file(client, filename)
            else:
                print(f"File {filename} does not exist.")
        
        elif choice == "2":
            filename = input("Enter the filename to download: ")
            download_file(client, filename)

        elif choice == "3":
            client.close()
            break

if __name__ == "__main__":
    main()
