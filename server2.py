import socket

def xor(a, b): return "".join("1" if a[i] != b[i] else "0" for i in range(1, len(b)))

def crc_check(codeword, generator):
    temp, n = codeword[:len(generator)], len(generator)
    for i in range(len(generator), len(codeword)):
        temp = xor(temp, generator if temp[0] == "1" else "0" * n) + codeword[i]
    return xor(temp, generator)[1:] if temp[0] == "1" else temp[1:]

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 6000))
    server.listen(1)
    conn, _ = server.accept()

    codeword, generator = conn.recv(1024).decode(), conn.recv(1024).decode()
    error_pos = int(conn.recv(1024).decode())
    conn.sendall(crc_check(codeword, generator).encode())
    corrupted = list(codeword)
    corrupted[-error_pos - 1] = "1" if corrupted[-error_pos - 1] == "0" else "0"
    conn.sendall(crc_check("".join(corrupted), generator).encode())

    conn.close()
    server.close()

if __name__ == "__main__":
    main()
