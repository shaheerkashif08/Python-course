from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def hello_world():
    if(request.method=="POST"):
        # Handle the form
        with open("file.txt", "w") as f:
            f.write(f"The name of client is {request.form['name']} and email id is {request.form['email']}")

    else:
        return render_template('04_contact-form.html') 


app.run(debug=True)