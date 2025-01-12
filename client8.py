import socket
import struct

def send_data_to_server(data):
    try:
        # Create a socket and connect to the server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 12345))

        # Send data to the server
        client.send(data)

        # Receive the checksum from the server
        checksum = client.recv(1024)
        checksum = struct.unpack('!H', checksum)[0]  # Unpack checksum as unsigned short
        print(f"Checksum received from server: {checksum}")

        client.close()

    except Exception as e:
        print(f"Error: {e}")

def main():
    data = input("Enter data to send to the server: ").encode()
    send_data_to_server(data)

if __name__ == "__main__":
    main()
