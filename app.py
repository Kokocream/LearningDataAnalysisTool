from flask import Flask

app = Flask(__name__)

if __name__ == "__main__" :
    app.run(debug=True, port=8080)

@app.route('/') # 装饰器 , 用来告诉Flask URL如何触发视图函数
def hello_world() :
    return '<p>Hello, World!<p>'