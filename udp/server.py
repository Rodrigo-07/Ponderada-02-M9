import socket

def main():
    host = "0.0.0.0"
    port = 6565

    # Cria um socket UDP normal
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print(f"Servidor UDP em {host}:{port}...")

    while True:
        # Recebe até 1024 bytes
        data, addr = sock.recvfrom(1024)
        print(f"[{addr}] Recebeu: {data}")

if __name__ == "__main__":
    main()
