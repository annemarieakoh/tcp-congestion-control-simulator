import socket
import random
import time

HOST = '127.0.0.1'
PORT = 12345
PACKET_LOSS_RATE = 0.2  # 20% packet loss simulation

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break

    if random.random() < PACKET_LOSS_RATE:  # Simulating packet loss
        print("Packet lost!")
        continue

    print(f"Received: {data.decode()}")
    time.sleep(0.5)  # Simulate network delay
    conn.sendall(b"ACK")

conn.close()
server_socket.close()