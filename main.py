from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# Recall this is to test a pipeline you're building
# For versioning, change the if check to have quick checks of whether
#it works
# Apparently you can have it run automatically with python
#   no need for flask run --app main or smoething lik ethat

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/time")
def get_time():
    x = time.localtime()
    if(x.tm_sec < 10):
        result = {"time": f"{x.tm_hour}:{x.tm_min}:0{x.tm_sec}"}
        return result
    result = {"time": f"{x.tm_hour}:{x.tm_min}:{x.tm_sec}"}
    return result

