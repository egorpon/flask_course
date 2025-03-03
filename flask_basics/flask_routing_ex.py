from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!"

@app.route("/puppy_latin/<name>")
def puppy_latin(name):
    if name[-1]!="y":
        return f"<h1>{name+"y"}</h1>"
    else:
        return f"<h1>{name[:-1]+"iful"}</h1>"
        
    



if __name__ == "__main__":
    app.run(debug=True)