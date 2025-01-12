import socket
import time

def ping_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("localhost", 12345)
    client.settimeout(1)  # Wait for up to 1 second for the reply

    for i in range(1, 11):  # Send 10 ping messages
        message = f"Ping {i}"
        start_time = time.time()

        # Send ping message
        client.sendto(message.encode(), server_address)

        try:
            # Receive pong message
            data, _ = client.recvfrom(1024)
            rtt = (time.time() - start_time) * 1000  # Convert to milliseconds
            print(f"Received from server: {data.decode()} | RTT = {rtt:.2f} ms")
        except socket.timeout:
            print(f"Ping {i} lost (no response)")

    client.close()

if __name__ == "__main__":
    ping_server()
