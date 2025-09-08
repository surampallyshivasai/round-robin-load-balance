# 🔀 Round Robin Load Balancer (Python + Flask)

A minimal Python project demonstrating how a **Load Balancer** works by distributing client requests across multiple backend servers using the **Round Robin algorithm**.

## 🚀 Features
- Round Robin request distribution
- Two backend servers (`server1.py`, `server2.py`)
- Simple Flask-based implementation
- Demonstrates basic **system design** concepts

## ⚡ How to Run

1. **Start backend servers (two terminals):**
   ```bash
   python server1.py
   python server2.py


Start the load balancer (third terminal):

python load_balancer.py


Send requests:

curl http://127.0.0.1:5000/request


✅ The requests will alternate between Server 1 and Server 2.

🛠️ Tech Stack

Python

Flask

Requests

📌 Example Output
{
  "forwarded_to": "http://127.0.0.1:5001/process",
  "server_response": {
    "server": "Server 1",
    "status": "success"
  }
}

🎯 Future Improvements

Add Least Connections algorithm

Add Health checks & self-healing

Add Metrics dashboard for real-time monitoring

Dockerize for scalable deployments

👤 Author

Shiva Sai Surampally

GitHub

LinkedIn


---

👉 Steps to add this:
1. Create a file in your project folder:


README.md

2. Paste the above content.  
3. Commit & push:
```bash
git add README.md
git commit -m "Added README.md"
git push


