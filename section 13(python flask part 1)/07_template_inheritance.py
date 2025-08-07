from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("07_home.html")

@app.route("/about")
def about():
    return render_template("07_about.html")

@app.route("/contact")
def contact():
    return render_template("07_contact.html")

if __name__ == "__main__":
    app.run(debug=True)
