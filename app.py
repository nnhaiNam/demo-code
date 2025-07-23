from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Harinem 642004!!!!!!'

# if __name__=="__main__":
#     app.run(debug=True)