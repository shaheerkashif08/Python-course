from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("02_home.html")

@app.route("/services")
def services():
    return render_template("02_services.html")

@app.route("/contact")
def contact():
    return render_template("02_contact.html")

@app.route("/about")
def about():
    return render_template("02_about.html")

app.run(debug=True)