import socket
import time

HOST = '127.0.0.1'
PORT = 12345

initial_cwnd = 2
timeout = 1

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

cwnd = initial_cwnd
seq_num = 0
rtt = 0.1  # Initial RTT estimate

while seq_num < 20:
    print(f"Sending {cwnd} packets...")
    start_time = time.time()
    
    for _ in range(cwnd):
        message = f"Packet {seq_num}".encode()
        client_socket.sendall(message)
        seq_num += 1

    client_socket.settimeout(timeout)
    try:
        ack = client_socket.recv(1024)
        end_time = time.time()
        rtt = (end_time - start_time) * 0.8 + rtt * 0.2
        cwnd = int(1 / rtt)  # Adjust window based on estimated bandwidth
        print(f"ACK received, updating cwnd to {cwnd} (based on RTT)")
    except socket.timeout:
        print("Packet loss detected! Reducing window size...")
        cwnd = max(1, cwnd // 2)

    time.sleep(0.5)

client_socket.close()