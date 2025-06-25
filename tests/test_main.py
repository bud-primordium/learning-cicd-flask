# 从我们的应用代码中，导入 app 对象和 get_greeting 函数
from app.main import app, get_greeting


# 第一个测试函数，专门测试 get_greeting 这个业务逻辑函数
def test_get_greeting():
    """测试核心业务逻辑：确保问候语中包含特定文字。"""
    # assert（断言）是测试的核心，如果后面的条件为False，测试就会失败
    assert "Advanced CI/CD" in get_greeting()


# 第二个测试函数，测试整个Web路由是否正常工作
def test_hello_world_route():
    """测试Flask路由：模拟一次网页访问，检查返回状态和内容。"""
    # 创建一个测试客户端，可以模拟浏览器向我们的app发送请求
    client = app.test_client()
    # 模拟向根地址 "/" 发送一个GET请求
    response = client.get("/")

    # 断言1: 检查HTTP状态码是不是200 (OK/成功)
    assert response.status_code == 200
    # 断言2: 检查返回的网页内容(response.data)中是否包含预期的字节字符串(b"...")
    assert b"Hello from our Advanced CI/CD pipeline!" in response.data
