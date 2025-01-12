import socket
import uuid

def get_client_ip_and_mac(client_socket):
    """Get the client's IP and MAC address."""
    # Get the client's IP address
    client_ip = client_socket.getpeername()[0]
    
    # Get the client's MAC address (we will just fetch the MAC of the local machine for demonstration)
    # In a real-world scenario, getting the remote client's MAC is not feasible over TCP/IP.
    # You'd typically use other methods, like ARP table or directly querying the client machine.
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                            for elements in range(0, 2 * 6, 2)][::-1])
    
    return client_ip, mac_address

def handle_client(client_socket):
    """Handle the connection with the client."""
    client_ip, mac_address = get_client_ip_and_mac(client_socket)
    print(f"Client IP: {client_ip}, Client MAC: {mac_address}")
    
    # Send the IP and MAC address back to the client
    message = f"Client IP: {client_ip}\nClient MAC: {mac_address}"
    client_socket.send(message.encode())

    client_socket.close()

def start_server():
    """Start the TCP server and listen for connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))  # Binding to localhost and port 8080
    server_socket.listen(5)
    print("Server is listening on port 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with: {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
