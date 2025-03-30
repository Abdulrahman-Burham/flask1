from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Azure!</h1><p>Welcome to your Flask Web App.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
