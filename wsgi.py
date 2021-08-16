from flask import Flask, render_template

app = Flask(__name__)

if __name__ == "__main__" :
    app.run(debug=True, port=8080)

@app.route('/') # 装饰器 , 用来告诉Flask URL如何触发视图函数
def home() :
    return render_template("base.html")

@app.route('/login') # 装饰器 , 用来告诉Flask URL如何触发视图函数
def login() :
    return 'Login or Register Page'


@app.route('/login') # 装饰器 , 用来告诉Flask URL如何触发视图函数
def visualize() :
    return 'Visualization Page'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s Personal File Page'    