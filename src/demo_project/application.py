import logging

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from demo_project.api.demo_api import router as demo_router
from demo_project.client.demo_sql_client import create_demo_sql_client
from demo_project.config.config import DATABASE_URL, DATABASE_USERNAME, DATABASE_PASSWORD
from demo_project.model.api_response import ApiResponse
from demo_project.service.demo_service import create_demo_service

_log = logging.getLogger(__name__)


# 创建所有实例
def create_instances():
    _log.info("Creating demo sql client")
    _log.info("Using database url: %s", DATABASE_URL)
    _log.info("Using database username: %s", DATABASE_USERNAME)
    _log.info("Using database password: %s", DATABASE_PASSWORD)
    demo_sql_client = create_demo_sql_client(DATABASE_URL, DATABASE_USERNAME, DATABASE_PASSWORD)

    _log.info("Creating demo service")
    create_demo_service(demo_sql_client)
    
    _log.info("All instances loaded")


# 创建应用程序实例
def create_app() -> FastAPI:
    # 创建FastAPI应用程序实例
    app: FastAPI = FastAPI(
        title="Demo FastAPI Application",
        version="1.0.0",
        description="A demo application with FastAPI"
    )

    create_instances()

    # 添加路由，统一前缀为/demo
    app.include_router(demo_router, prefix="/demo", tags=["demo"])

    # 全局异常处理器
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        # 记录详细错误信息
        _log.error(f"Unhandled exception at {request.url}: {exc}")
        return JSONResponse(status_code=200, content=ApiResponse(success=False, message="服务器内部错误").model_dump())

    # 返回应用程序实例
    return app


# 创建应用程序实例
app: FastAPI = create_app()
_log.info("FastAPI应用程序已创建")
