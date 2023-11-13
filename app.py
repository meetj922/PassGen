from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

def generate_password(length, include_upper=True, include_numbers=True, include_special=True):
    characters = string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_password", methods=["POST"])
def generate_password_route():
    try:
        length = int(request.form.get("length"))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")

        include_upper = "include_upper" in request.form
        include_numbers = "include_numbers" in request.form
        include_special = "include_special" in request.form

        password = generate_password(length, include_upper, include_numbers, include_special)
        
        return render_template("index.html", password=password)
    except ValueError as e:
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
