import uvicorn

# 开发环境启动方法 生产环境勿用
if __name__ == "__main__":
    uvicorn.run("demo_project.application:app", host="0.0.0.0", port=8080, reload=True)
