from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')
@app.route('/login',methods=["POST"])
def login():
    if request.method=="POST":
        user = request.form["nm"]
        return render_template("app.html",y=user)
@app.route('/hello')
def hello_world():
    return "hello world"
@app.route('/logged')
def logged():
    return "User Logged in"
if __name__ =='__main__':
    app.run(debug = True)