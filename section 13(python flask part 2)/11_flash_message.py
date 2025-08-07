from flask import Flask, flash, render_template

app = Flask(__name__)
app.secret_key = "nxn3nx3nxns5n6b5nb4bu3u2"

@app.route("/")
def hello_world():
    return render_template("11_index.html")

@app.route("/logout")
def logout():
    flash("You have been logged out!")
    return render_template("11_index.html")

app.run(debug=True)