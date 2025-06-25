# 从 flask 包中导入 Flask 类
from flask import Flask

# 创建一个Flask应用的实例（你可以把它想象成我们的Web服务器对象）
app = Flask(__name__)


# 定义一个普通的Python函数，它返回一个字符串
# -> str 就是类型注解，表示这个函数应该返回一个字符串(string)
def get_greeting() -> str:
    """这是一个文档字符串，解释函数的作用：返回一个问候语。"""
    return "Hello from our Advanced CI/CD pipeline!"


# 这是一个“路由装饰器”，它告诉Flask：
# 当有用户访问网站的根地址("/")时，就执行下面的 hello_world 函数
@app.route("/")
def hello_world() -> str:
    """Web应用的根路由，它会调用get_greeting()并返回结果。"""
    return get_greeting()


# 这是一个Python的常用技巧
# 只有当你直接运行这个文件时(python app/main.py)，下面的代码才会执行
# 如果这个文件是被其他文件导入的，这部分就不会执行
# 这使得它很适合用来做本地开发测试
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
