```python
# test/run_test.py
import pytest

# 测试运行方法
if __name__ == "__main__":
    pytest.main()

# test/demo_project_test/application_test.py
from fastapi.testclient import TestClient

from demo_project.application import app

# 创建FastAPI测试客户端
client = TestClient(app, raise_server_exceptions=False)


# 测试 POST /demo/demo 端点
def test_post_demo_endpoint():
    # 准备请求数据和响应数据
    request_body = {
        "id": 999,
        "name": "Test Item",
        "description": "This is a test item for API testing"
    }
    response_body = {
        "success": True,
        "message": "success",
        "data": {
            "id": 999,
            "name": "Test Item",
            "description": "This is a test item for API testing",
        },
        "extra": None,
    }

    # 发送POST请求到/demo端点
    response = client.post("/demo/demo", json=request_body)

    # 验证响应状态码和响应内容结构
    assert response.status_code == 200
    assert response.json() == response_body


# 测试 POST /demo/demo 端点的无效数据验证
def test_post_demo_endpoint_with_invalid_data():
    # 准备无效请求数据（id为负数）和响应数据
    request_body = {
        "id": -1,
        "name": "Invalid Item",
        "description": "This item has invalid id"
    }
    response_body = {
        "detail": [
            {
                "type": "value_error",
                "loc": ["body", "id"],
                "msg": "Value error, id must be positive",
                "input": -1,
                "ctx": {
                    "error": {},
                },
            }
        ]
    }

    # 发送POST请求到/demo端点
    response = client.post("/demo/demo", json=request_body)

    # 验证响应状态码和响应内容结构
    assert response.status_code == 422
    assert response.json() == response_body


# 测试 POST /demo/error 异常接口
def test_post_error_endpoint():
    # 准备响应数据
    response_body = {
        "success": False,
        "message": "服务器内部错误",
        "data": None,
        "extra": None,
    }

    # 发送POST请求到/error端点
    response = client.post("/demo/error")

    # 验证响应状态码和响应内容结构
    assert response.status_code == 200
    assert response.json() == response_body
```
