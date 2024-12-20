# from flask import Flask

# app=Flask(__name__)

# @app.route("/hello")
# def hello_world():
#     return "Hello, World!"

# app.run()


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)  # debug=True for auto-reload
 