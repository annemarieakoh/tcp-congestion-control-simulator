import socket
import time
import matplotlib.pyplot as plt
import csv

HOST = '127.0.0.1'
PORT = 12345

initial_cwnd = 1
ssthresh = 8
timeout = 1

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

cwnd = initial_cwnd
seq_num = 0

# For plotting
cwnd_history = []
time_history = []
start_time = time.time()

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
        print("Packet loss detected! Resetting to slow start...")
        ssthresh = cwnd // 2
        cwnd = 1

    # Log cwnd value and timestamp
    cwnd_history.append(cwnd)
    time_history.append(time.time() - start_time)

    time.sleep(0.5)

client_socket.close()

# Plotting the cwnd vs. time
plt.plot(time_history, cwnd_history, marker='o')
plt.title('TCP Tahoe: cwnd over Time')
plt.xlabel('Time (s)')
plt.ylabel('Congestion Window Size (cwnd)')
plt.grid(True)
#plt.show()

# Save cwnd history to CSV
with open("tahoe_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "CWND"])
    for t, w in zip(time_history, cwnd_history):
        writer.writerow([t, w])
