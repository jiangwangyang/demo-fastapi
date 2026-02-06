# test 代码编写规范

## 定位说明

- test 目录用于存放测试用例与测试入口。
- 测试用例应覆盖核心接口与关键业务路径。

## 目录与文件规范

- 测试入口文件为 `test/run_test.py`。
- 测试用例存放在 `test/demo_project_test/` 目录下。
- 测试文件名必须以 `_test.py` 结尾。
- 测试文件必须显式导入被测模块，不允许动态导入。

## 测试函数格式规范（强制）

- 每个测试函数必须按以下顺序组织：
  1) 开头给出输入与输出（request/response 或 input/expected）。
  2) 调用要测试的方法或接口。
  3) 验证结果（status_code 与内容、或返回值）。
- 测试函数必须独立、可重复执行。
- 禁止使用二级列表。

## 变量与命名规范

- 变量必须显式声明类型。
- 变量命名遵循 `语义 + 类型后缀`。
- 例如：`request_body_dict: dict`, `response_body_dict: dict`，`client: TestClient`。
- 禁止使用 `dict` 作为函数入参类型。

## 依赖与使用规范

- Web 接口测试统一使用 `TestClient`。
- 统一从 `demo_project.application` 导入 `app`。
- 断言必须覆盖响应状态码与响应体结构。

## 示例

```python
from fastapi.testclient import TestClient

from demo_project.application import app

client: TestClient = TestClient(app)

# 测试 POST /demo/demo 端点
def test_post_demo_endpoint() -> None:
    # 准备请求数据和响应数据
    request_body_dict: dict = {
        "id": 999,
        "name": "Test Item",
        "description": "This is a test item for API testing"
    }
    response_body_dict: dict = {
        "success": True,
        "message": "success",
        "data": {
            "id": 999,
            "name": "Test Item",
            "description": "This is a test item for API testing"
        },
        "extra": None
    }

    # 发送POST请求到/demo端点
    response = client.post("/demo/demo", json=request_body_dict)

    # 验证响应状态码和响应内容结构
    assert response.status_code == 200
    assert response.json() == response_body_dict
```
