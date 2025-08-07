from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/")
def json():
    marks={
        "Samarth": 76,
        "Abhishek": 67,
        "Rubina": 88,
        "Jannat": 56,
        "Reem": 56,
        "Ali": 89,
        "Rahul": 78
    }
    return jsonify([1, marks, 76])
    

app.run(debug=True)