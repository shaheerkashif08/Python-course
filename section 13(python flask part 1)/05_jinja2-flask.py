from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Samarth": 76,
        "Abhishek": 60,
        "Rubina": 98,
        "Rahul": 85,
        "Vicky": 88,
        "Krishna": 65,
        "Abdu": 71,
        "Elvish": 69
    }
    return render_template("05_index.html", marks=marks)

app.run(debug=True)