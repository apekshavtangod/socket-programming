import socket

def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        result += "1" if a[i] != b[i] else "0"
    return result

def crc_check(codeword, generator):
    n = len(generator)
    temp = codeword[:n]
    for i in range(n, len(codeword)):
        if temp[0] == "1":
            temp = xor(temp, generator) + codeword[i]
        else:
            temp = xor(temp, "0" * len(generator)) + codeword[i]
    
    if temp[0] == "1":
        temp = xor(temp, generator)
    
    return temp[1:]

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(1)
    print("Server is listening for connections...")
    
    conn, addr = server.accept()
    print(f"Connected to client: {addr}")

    # Receive the codeword and generator from the client
    codeword = conn.recv(1024).decode()
    generator = conn.recv(1024).decode()

    print(f"Received codeword: {codeword}")
    print(f"Received generator: {generator}")

    # Perform CRC check
    remainder = crc_check(codeword, generator)
    print(f"Calculated remainder: {remainder}")

    # Send the remainder back to the client
    conn.sendall(remainder.encode())

    conn.close()
    server.close()

if __name__ == "__main__":
    main()
