# TCP Congestion Control Simulator

This project simulates and visualizes the behavior of different TCP congestion control algorithms under simulated network congestion using a custom server-client setup.

## Algorithms Implemented

- **TCP Tahoe** – Resets to Slow Start after packet loss
- **TCP Reno** – Halves window size after loss
- **TCP Cubic** – Uses a cubic growth function for cwnd
- **TCP BBR** – Estimates bandwidth and RTT, not loss-driven

---

## How It Works

- A Python-based server simulates network congestion by randomly dropping packets.
- Each client implements a different TCP congestion control algorithm.
- Clients log the congestion window (`cwnd`) over time to a `.csv` file.
- Graphical visualization script shows how each algorithm adapts to congestion.

---

##  How to Run

### Install dependencies with
pip install matplotlib

### 1. Start the Server
python server.py

### 2. Run each Client at a time
python tahoe_client.py
python reno_client.py
python cubic_client.py
python bbr_client.py

### 3. Move the generated csv log files to the result_csv directory

### 4. Run the python script to plot all results on the same graph
python plot_all.py