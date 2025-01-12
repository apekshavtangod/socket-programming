import socket
import struct

# Function to calculate the Internet checksum
def internet_checksum(data):
    # Ensure data is even-length (pad with 0 if necessary)
    if len(data) % 2 != 0:
        data += b'\x00'

    checksum = 0
    for i in range(0, len(data), 2):
        word = struct.unpack('!H', data[i:i+2])[0]  # Convert two bytes to an unsigned short
        checksum += word
        checksum = (checksum & 0xFFFF) + (checksum >> 16)  # Handle overflow

    # Return the one's complement of the checksum
    return ~checksum & 0xFFFF

def handle_client(client_socket):
    try:
        # Receive data from the client
        data = client_socket.recv(1024)

        # Calculate the checksum
        checksum = internet_checksum(data)
        
        # Send the checksum back to the client
        client_socket.send(struct.pack('!H', checksum))

    except Exception as e:
        print(f"Error: {e}")
        client_socket.send(b"Error processing data")

    finally:
        client_socket.close()

def server_main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))  # Port 12345 for checksum service
    server.listen(5)
    print("Checksum server is listening on port 12345...")

    while True:
        client_socket, _ = server.accept()
        handle_client(client_socket)

if __name__ == "__main__":
    server_main()
