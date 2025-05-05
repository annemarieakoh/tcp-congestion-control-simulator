import socket
import time
import math

HOST = '127.0.0.1'
PORT = 12345

initial_cwnd = 1
timeout = 1
C = 0.4  # Cubic scaling factor
W_max = 10  # Target maximum window size

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
        print("ACK received, adjusting cubic growth...")
        cwnd = math.floor(W_max * (C * ((seq_num / W_max) ** 3))) + 1
    except socket.timeout:
        print("Packet loss detected! Reducing window size...")
        cwnd = max(1, cwnd // 2)

    time.sleep(0.5)

client_socket.close()