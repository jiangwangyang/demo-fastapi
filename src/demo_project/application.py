import logging

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from demo_project.api.demo_api import router as demo_router
from demo_project.client.demo_sql_client import get_demo_sql_client
from demo_project.model.api_response import ApiResponse
from demo_project.service.demo_service import get_demo_service

_log = logging.getLogger(__name__)

# 获取所有实例，用于启动时加载所有模块
demo_service = get_demo_service()
demo_sql_client = get_demo_sql_client()
_log.info("所有实例已加载")


# 创建应用程序实例
def create_app() -> FastAPI:
    # 创建FastAPI应用程序实例
    app: FastAPI = FastAPI(
        title="Demo FastAPI Application",
        version="1.0.0",
        description="A demo application with FastAPI"
    )

    # 添加路由，统一前缀为/demo
    app.include_router(demo_router, prefix="/demo", tags=["demo"])

    # 全局异常处理器
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        # 记录详细错误信息
        _log.error(f"Unhandled exception at {request.url}: {exc}")
        return JSONResponse(status_code=200, content=ApiResponse(success=False, message="服务器内部错误"))

    # 返回应用程序实例
    return app


# 创建应用程序实例
app: FastAPI = create_app()
_log.info("FastAPI应用程序已创建")
