import socket
import time

HOST = '127.0.0.1'
PORT = 12345

initial_cwnd = 1  # Start slow
ssthresh = 8  # Slow start threshold
timeout = 1  # 1-second timeout for ACKs

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
            cwnd *= 2  # Exponential increase (Slow Start)
        else:
            cwnd += 1  # Linear increase (Congestion Avoidance)
    except socket.timeout:
        print("Packet loss detected! Resetting to slow start...")
        ssthresh = cwnd // 2  # Reduce threshold
        cwnd = 1  # Reset to Slow Start

    time.sleep(0.5)

client_socket.close()