from flask import Flask

app = Flask(__name__)

@app.route("/")    # '/' For the home page
def hello_world():
  return "Hello World."

print(__name__)
if __name__=="__main__":
  print("I'm inside the if now")
  app.run(host="0.0.0.0",debug=True)