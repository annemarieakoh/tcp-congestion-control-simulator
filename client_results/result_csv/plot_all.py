#script to load all CSV logs and creates a line graph

import matplotlib.pyplot as plt
import csv

def read_log(filename):
    times = []
    cwnds = []
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            times.append(float(row[0]))
            cwnds.append(int(row[1]))
    return times, cwnds

# Load all logs
tahoe_t, tahoe_w = read_log("tahoe_log.csv")
reno_t, reno_w = read_log("reno_log.csv")
cubic_t, cubic_w = read_log("cubic_log.csv")
bbr_t, bbr_w = read_log("bbr_log.csv")

# Plot
plt.figure(figsize=(10, 6))
plt.plot(tahoe_t, tahoe_w, label="Tahoe", marker='o')
plt.plot(reno_t, reno_w, label="Reno", marker='x')
plt.plot(cubic_t, cubic_w, label="Cubic", marker='s')
plt.plot(bbr_t, bbr_w, label="BBR", marker='^')

plt.title("TCP Congestion Control Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Congestion Window Size (CWND)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
