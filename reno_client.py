import socket
import time

HOST = '127.0.0.1'
PORT = 12345

initial_cwnd = 1
ssthresh = 8
timeout = 1

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

cwnd = initial_cwnd
seq_num = 0

while seq_num < 20:
    print(f"Sending {cwnd} packets...")
    for _ in range(cwnd):
        message = f"Packet {seq_num}".encode()
        client_socket.sendall(message)
        seq_num += 1

    client_socket.settimeout(timeout)
    try:
        ack = client_socket.recv(1024)
        print("ACK received, increasing window size...")
        if cwnd < ssthresh:
            cwnd *= 2
        else:
            cwnd += 1
    except socket.timeout:
        print("Packet loss detected! Halving congestion window...")
        ssthresh = cwnd // 2
        cwnd = max(1, cwnd // 2)

    time.sleep(0.5)

client_socket.close()