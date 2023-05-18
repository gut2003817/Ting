from flask import Flask
app = Flask(__name__)

from flask import request
from flask import render_template

# 驗證登入函式
def valid_login(user, passwd):
    # 檢查使用者名稱和密碼是否有效
    if user == "test" and passwd == "1234":
        return True
    else:
        return False

# 使用者登入函式
def log_the_user_in(user):
    # 回傳登入成功訊息
    return user + "登入成功"

@app.route('/login', methods=['POST', 'GET'])
#實作/login 可以吃POST、GET Method，login.html，若驗證成功顯示歡迎訊息
def login():
    return""

if __name__ == '__main__':
    app.run(debug=True)