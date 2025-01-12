import socket

# Simplified DNS records: mapping domain names to IP addresses
dns_records = {
    "www.google.com": "142.250.72.14",
    "www.facebook.com": "157.240.22.35",
    "www.github.com": "140.82.113.3",
    "www.example.com": "93.184.216.34"
}

def handle_client(client_socket):
    try:
        # Receive the domain name from the client
        domain_name = client_socket.recv(1024).decode()
        print(f"Received domain name: {domain_name}")
        
        # Resolve domain name to IP address
        ip_address = dns_records.get(domain_name, "Domain not found")
        
        # Send the corresponding IP address (or error message) back to the client
        client_socket.send(ip_address.encode())

    except Exception as e:
        print(f"Error: {e}")
        client_socket.send(b"Error processing request")
    finally:
        client_socket.close()

def server_main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 53))  # Port 53 is typically used for DNS
    server.listen(5)
    print("DNS server is listening on port 53...")

    while True:
        client_socket, _ = server.accept()
        handle_client(client_socket)

if __name__ == "__main__":
    server_main()
