from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def receive_data():
    name = request.form.get('username')
    password = request.form.get('password')
    return f"Form submitted! User: {name} - Password: {password}"

if __name__ == '__main__':
    app.run(debug=True)