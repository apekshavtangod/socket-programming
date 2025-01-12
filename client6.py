import socket

def send_request(client_socket, request):
    client_socket.send(request.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    while True:
        print("1. Check Balance")
        print("2. View Transaction History")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_id = input("Enter account ID: ")
            send_request(client, f"BALANCE {account_id}")

        elif choice == "2":
            account_id = input("Enter account ID: ")
            send_request(client, f"HISTORY {account_id}")

        elif choice == "3":
            account_id = input("Enter account ID: ")
            amount = float(input("Enter amount to deposit: "))
            send_request(client, f"DEPOSIT {account_id} {amount}")

        elif choice == "4":
            account_id = input("Enter account ID: ")
            amount = float(input("Enter amount to withdraw: "))
            send_request(client, f"WITHDRAWAL {account_id} {amount}")

        elif choice == "5":
            print("Goodbye!")
            client.close()
            break

if __name__ == "__main__":
    main()
