import socket
import os
import threading
import time

BUFFER_SIZE = 1024
WINDOW_SIZE = 5

def handle_client(conn, addr):
    print(f"Connected to {addr}")
    filename = conn.recv(BUFFER_SIZE).decode()
    if not os.path.exists(filename):
        conn.sendall(b"ERROR: File not found")
        conn.close()
        return

    conn.sendall(b"OK")
    with open(filename, "rb") as f:
        chunks = [f.read(BUFFER_SIZE) for _ in iter(lambda: True, b"")]
    
    base, next_seq, acked = 0, 0, set()
    total_chunks = len(chunks)

    while base < total_chunks:
        while next_seq < min(base + WINDOW_SIZE, total_chunks):
            conn.sendall(f"{next_seq}".encode().ljust(10) + chunks[next_seq])
            next_seq += 1

        try:
            conn.settimeout(2)
            ack = int(conn.recv(10).decode().strip())
            if ack >= base:
                base = ack + 1
                acked.add(ack)
        except socket.timeout:
            next_seq = base  # Resend unacknowledged chunks

    conn.sendall(b"COMPLETE")
    print(f"File transfer to {addr} completed.")
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(5)
    print("Server is listening for connections...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
