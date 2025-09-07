import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Backend servers list
servers = ["http://127.0.0.1:5001/process", "http://127.0.0.1:5002/process"]
current = 0  # keeps track of round-robin position

@app.route("/request", methods=["GET"])
def load_balance():
    global current

    # Pick server using round robin
    server = servers[current]
    current = (current + 1) % len(servers)

    try:
        response = requests.get(server, timeout=3)
        return jsonify({
            "forwarded_to": server,
            "server_response": response.json()
        })
    except Exception as e:
        return jsonify({"error": str(e), "server": server})

if __name__ == "__main__":
    app.run(port=5000)

