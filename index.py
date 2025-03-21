from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")






@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("r4iner")  
    return render_template("welcome.html", name=user) 

@app.route("/")
def index():
    homepage = "<h1>郭碩元Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=tcyang>傳送使用者暱稱</a><br>"
    homepage += "<a href=/account>網頁表單傳值</a><br>"
    homepage += "<a href=/about>郭碩元簡介網頁</a><br>"
    return homepage





    return "hello 郭碩元!"

@app.route("/mis")
def course():
    return "<h1>郭碩元</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime=str(now))

if __name__ == "__main__":
    app.run()
