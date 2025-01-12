import socket
import os

BUFFER_SIZE = 1024
WINDOW_SIZE = 5

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5000))

    filename = input("Enter the filename to download: ")
    client.sendall(filename.encode())

    response = client.recv(BUFFER_SIZE).decode()
    if response != "OK":
        print(response)
        client.close()
        return

    with open(f"downloaded_{filename}", "wb") as f:
        expected_seq, completed = 0, False

        while not completed:
            data = client.recv(BUFFER_SIZE + 10)
            if data.startswith(b"COMPLETE"):
                completed = True
            else:
                seq_num = int(data[:10].decode().strip())
                if seq_num == expected_seq:
                    f.write(data[10:])
                    client.sendall(f"{seq_num}".encode().ljust(10))
                    expected_seq += 1
                else:
                    client.sendall(f"{expected_seq - 1}".encode().ljust(10))  # Acknowledge the last correct packet

    print("File downloaded successfully.")
    client.close()

if __name__ == "__main__":
    main()
