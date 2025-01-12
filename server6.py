import socket
import threading

# Bank account details
accounts = {"12345": {"balance": 1000, "history": []}}

def handle_client(client_socket):
    try:
        # Client's request
        request = client_socket.recv(1024).decode()
        print(f"Request from client: {request}")
        
        if request.startswith("BALANCE"):
            account_id = request.split()[1]
            if account_id in accounts:
                balance = accounts[account_id]["balance"]
                client_socket.send(f"Balance: {balance}".encode())
            else:
                client_socket.send(b"Invalid account ID")

        elif request.startswith("HISTORY"):
            account_id = request.split()[1]
            if account_id in accounts:
                history = "\n".join(accounts[account_id]["history"])
                client_socket.send(history.encode())
            else:
                client_socket.send(b"Invalid account ID")

        elif request.startswith("DEPOSIT"):
            account_id, amount = request.split()[1], float(request.split()[2])
            if account_id in accounts:
                accounts[account_id]["balance"] += amount
                accounts[account_id]["history"].append(f"Deposited {amount}")
                client_socket.send(f"Deposited {amount} to account {account_id}".encode())
            else:
                client_socket.send(b"Invalid account ID")

        elif request.startswith("WITHDRAWAL"):
            account_id, amount = request.split()[1], float(request.split()[2])
            if account_id in accounts:
                if accounts[account_id]["balance"] >= amount:
                    accounts[account_id]["balance"] -= amount
                    accounts[account_id]["history"].append(f"Withdrew {amount}")
                    client_socket.send(f"Withdrew {amount} from account {account_id}".encode())
                else:
                    client_socket.send(b"Insufficient balance")
            else:
                client_socket.send(b"Invalid account ID")

        else:
            client_socket.send(b"Invalid request")

    except Exception as e:
        print(f"Error: {e}")
        client_socket.send(b"Error processing request")

    finally:
        client_socket.close()

def server_main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(5)
    print("Server is listening on port 12345...")

    while True:
        client_socket, _ = server.accept()
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    server_main()
