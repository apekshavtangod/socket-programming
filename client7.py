import socket

def dns_query(domain_name):
    try:
        # Create a socket and connect to the DNS server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 53))
        
        # Send the domain name to the server
        client.send(domain_name.encode())
        
        # Receive the IP address (or error message) from the server
        ip_address = client.recv(1024).decode()
        print(f"Resolved IP address for {domain_name}: {ip_address}")
        
        client.close()
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\nEnter a domain name to resolve (or 'exit' to quit): ")
        domain_name = input()
        
        if domain_name.lower() == "exit":
            print("Exiting DNS client.")
            break
        
        # Query the DNS server for the domain name
        dns_query(domain_name)

if __name__ == "__main__":
    main()
