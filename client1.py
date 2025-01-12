import socket

def xor(a, b):
    result = ""
    for i in range(len(b)):
        result += "1" if a[i] != b[i] else "0"
    return result

def crc_generate(data, generator):
    n = len(generator)
    appended_data = data + "0" * (n - 1)
    temp = appended_data[:n]
    for i in range(n, len(appended_data)):
        if temp[0] == "1":
            temp = xor(temp, generator) + appended_data[i]
        else:
            temp = xor(temp, "0" * len(generator)) + appended_data[i]

    if temp[0] == "1":
        temp = xor(temp, generator)

    return data + temp[1:]

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5000))

    data = "101101"
    generator = "1101"
    codeword = crc_generate(data, generator)
    print(f"Generated codeword: {codeword}")

    # Send the codeword and generator to the server
    client.sendall(codeword.encode())
    client.sendall(generator.encode())

    # Receive the remainder from the server
    remainder = client.recv(1024).decode()

    if remainder:
        print(f"Received remainder from server: {remainder}")
        if int(remainder) == 0:
            print("No error detected in the transmitted codeword.")
        else:
            print("Error detected in the transmitted codeword.")
    else:
        print("No response received from server.")

    client.close()

if __name__ == "__main__":
    main()
