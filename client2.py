import socket

def xor(a, b): return "".join("1" if a[i] != b[i] else "0" for i in range(1, len(b)))

def crc_generate(data, generator):
    appended = data + "0" * (len(generator) - 1)
    temp = appended[:len(generator)]
    for i in range(len(generator), len(appended)):
        temp = xor(temp, generator if temp[0] == "1" else "0" * len(generator)) + appended[i]
    return data + xor(temp, generator)[1:] if temp[0] == "1" else data + temp[1:]

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 6000))

    data, generator, error_pos = "1010011101", "10011", 5
    codeword = crc_generate(data, generator)
    print(f"Generated codeword: {codeword}")

    for msg in [codeword, generator, str(error_pos)]:
        client.sendall(msg.encode())
    
    print(f"Syndrome (no error): {client.recv(1024).decode()}")
    print(f"Syndrome (with error): {client.recv(1024).decode()}")

    client.close()

if __name__ == "__main__":
    main()
