from flask import Flask, render_template, request, jsonify
from torch import load as load_network
import numpy as np

app = Flask(__name__)
net = load_network("digit_rec.pth")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_data", methods=["POST"])
def get_data():
    data = request.form["image"]
    arr = []
    for dat in data.split(","):
        print(dat)
        arr.append(int(dat))
    print(len(arr))
    arr = np.array(arr)
    arr = np.reshape(252, 252)
    new_data = []
    for i in range(9):
        for j in range(9):
            pass
    return jsonify("hi")

app.run(port=80, debug=True)