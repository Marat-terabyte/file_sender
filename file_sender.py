import socket
import sys

def main(address, port, filename):
    client = socket.socket()
    client.connect((address, port))

    print("Connected to the server")

    with open(filename, "rb") as f:
        while (True):
            data = f.read(4096)
            if not data:
                break

            client.sendall(data)
    
        print("File sent successfully")

if __name__ == "__main__":
    address = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]

    main(address, port, filename)