# application 代码编写规范

## 定位说明

- application 层用于应用初始化、依赖装配、全局上下文管理。
- application 层禁止编写任何业务逻辑。

## 文件与命名规范

- 应用入口文件必须为 `src/demo_project/application.py`。
- 允许在该文件中创建 FastAPI 实例与路由挂载。

## 依赖与职责规范

- application 层只负责组装依赖与加载路由。
- application 层可以显式加载 service/client 实例用于启动时初始化。
- application 层禁止直接调用任何业务处理流程。

## 实例创建规范

- 必须提供 `create_app()` 工厂函数用于创建 FastAPI 实例。
- 模块级必须暴露 `app: FastAPI` 变量作为启动入口。
- 路由注册必须通过 `app.include_router(...)` 完成。
- 路由只从 api 层导入，禁止从 service 或 client 层直接挂载。

## 异常处理规范

- 必须统一注册全局异常处理器。
- 异常响应必须使用统一的响应模型（如 `ApiResponse`）。
- 异常处理器内只允许记录日志与构造响应，禁止业务逻辑。

## 日志规范

- 必须使用 `__name__` 定义模块级 logger，且变量名为 `_log`。
- 启动过程的关键节点必须记录日志。

## 示例

```python
import logging

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from demo_project.api.demo_api import router as demo_router
from demo_project.model.api_response import ApiResponse
from demo_project.service.demo_service import get_demo_service
from demo_project.client.demo_sql_client import get_demo_sql_client

_log = logging.getLogger(__name__)

demo_service = get_demo_service()
demo_sql_client = get_demo_sql_client()


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(title="Demo FastAPI Application")
    app.include_router(demo_router, prefix="/demo", tags=["demo"])

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        _log.error(f"Unhandled exception at {request.url}: {exc}")
        return JSONResponse(status_code=200, content=ApiResponse(success=False, message="服务器内部错误"))

    return app

app: FastAPI = create_app()
```
