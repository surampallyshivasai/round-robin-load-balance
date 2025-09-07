from flask import Flask, request, jsonify
import time, random

app = Flask(__name__)

@app.route("/process", methods=["GET"])
def process():
    # simulate some work
    time.sleep(random.uniform(0.5, 2.0))
    return jsonify({"server": "Server 2", "status": "success"})

if __name__ == "__main__":
    app.run(port=5002)
