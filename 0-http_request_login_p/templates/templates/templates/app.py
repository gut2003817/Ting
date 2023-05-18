from flask import Flask
app = Flask(__name__)

from flask import request
from flask import render_template

users = {
    'user1': {
        'name': 'User One',
        'email': 'user1@example.com'
    },
    'user2': {
        'name': 'User Two',
        'email': 'user2@example.com'
    },
    'user3': {
        'name': 'User Three',
        'email': 'user3@example.com'
    },
    'user4': {
        'name': 'User Four',
        'email': 'user4@example.com'
    },
    'user5': {
        'name': 'User Five',
        'email': 'user5@example.com'
    },
}


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
    if request.method == "POST":
        return request.form["username"]
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)