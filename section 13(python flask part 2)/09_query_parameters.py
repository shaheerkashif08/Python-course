from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    # name="Harry"
    # token= 23
    name = request.args['name']
    token = request.args['tokens']
    return render_template("09_index.html", name=name, token= token)

app.run(debug=True)