import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("localhost", 12345))
    print("Server is listening...")

    while True:
        data, addr = server.recvfrom(1024)
        print(f"Received {data.decode()} from {addr}")
        server.sendto(data, addr)  # Echo the message back to the client

if __name__ == "__main__":
    main()
