from fastapi import FastAPI

from demo_project.api.test_api import router as test_router


# 创建应用程序实例
def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title="Demo FastAPI Application",
        version="1.0.0",
        description="A demo application with FastAPI"
    )

    # 添加路由，统一前缀为/demo
    app.include_router(test_router, prefix="/demo", tags=["demo"])

    @app.get("/")
    def read_root():
        return {"message": "Welcome to Demo FastAPI Application"}

    return app


# 创建应用程序实例
app: FastAPI = create_app()

# 开发环境可直接运行
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("demo_project.application:app", host="0.0.0.0", port=8080, reload=True)
