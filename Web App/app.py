from flask import Flask

app = Flask(__name__)


@app.route("/")
def run_Script():
    file = open(r'D:\GitHub Repos\Sorting-Vizualizers-with-Python\Using Tkinter\Sorting(Tkinter).py', 'r').read()
    return exec(file)


def home():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)