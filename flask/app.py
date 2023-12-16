from flask import Flask

app = Flask(__name__)

@app.route('/<greeting>')
def helloworld(greeting):
    return f"{greeting}, world!"

if __name__ == "__main__":
    app.run()
