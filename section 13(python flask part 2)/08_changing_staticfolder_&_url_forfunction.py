from flask import Flask, render_template

# app = Flask(__name__, static_url_path = "/static")   # This is how you change the url path
app = Flask(__name__, static_folder="assets", static_url_path = "/static")       # This is how you change the folder location

@app.route("/")
def hello_world():
    return render_template("08_index.html")

app.run(debug=True)