# TCP Congestion Control Simulator

This project simulates different TCP congestion control algorithms (Tahoe, Reno, Cubic, BBR) using custom clients and a loss-simulating server.

## 📌 How It Works

- `server.py`: Randomly drops packets to simulate network congestion.
- Each client simulates one congestion control algorithm:
  - `tahoe_client.py`
  - `reno_client.py`
  - `cubic_client.py`
  - `bbr_client.py`

## 🚀 How to Run

1. Start the server:
   ```bash
   python server.py
