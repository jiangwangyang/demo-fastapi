# Demo FastAPI Project

这是一个基于FastAPI的演示项目，遵循特定的项目结构规范。

## 项目结构

- `api/` - 接口层，负责参数接收与校验
- `service/` - 业务逻辑层，负责业务规则和编排
- `model/` - 数据模型层，定义数据结构
- `config/` - 配置定义层
- `client/` - 外部访问层
- `util/` - 通用工具层

## API端点

- `GET /` - 根路径，欢迎信息
- `GET /demo/test` - 测试端点
- `GET /demo/test/{item_id}` - 根据ID获取项目

## 安装与运行

```bash
# 安装依赖
pip install -e .

# 运行应用
python -m src.demo_project.main
```

或者直接运行：

```bash
python src/demo_project/application.py
```

应用将在 http://localhost:8080 启动。