from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('1.html')


@app.route("/login", methods=['post'])  # 因为账号密码要在浏览器上不显示，所以要用post方法，不能用get方法
def login():
    # 接受用户名和密码
    uername = request.form.get('username')
    pwd = request.form.get('pwd')
    if uername == 'abc' and pwd == '123':
        return '账号密码正确'
    else:
        return render_template('1.html', msg="登陆失败！")


if __name__ == '__main__':
    app.run()
