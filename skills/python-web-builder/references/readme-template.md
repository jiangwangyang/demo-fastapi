# {{项目名称}}

{{项目简介（1-2句）}}

## 项目结构

```
.
├── src/
│   ├── {{project_name}}/
│   │   ├── api/
│   │   │   └── {{module}}_api.py
│   │   ├── client/
│   │   │   └── {{module}}_client.py
│   │   ├── config/
│   │   │   ├── config.py
│   │   │   ├── config_dev.py
│   │   │   └── config_prod.py
│   │   ├── model/
│   │   │   ├── {{module}}_dto.py
│   │   │   ├── {{module}}_entity.py
│   │   │   └── {{module}}_vo.py
│   │   ├── service/
│   │   │   └── {{module}}_service.py
│   │   ├── util/
│   │   │   └── {{name}}_util.py
│   │   └── application.py
│   └── run_application.py
├── test/
│   ├── {{project_name}}_test/
│   │   └── application_test.py
│   └── run_test.py
├── .gitignore
├── AGENTS.md
├── README.md
├── pyproject.toml
└── uv.lock
```

- `api/` - 接口层，负责参数接收与校验
- `service/` - 业务逻辑层，负责业务规则和编排
- `model/` - 数据模型层，定义数据结构
- `config/` - 配置定义层
- `client/` - 外部访问层
- `util/` - 通用工具层

## API端点

- `{{METHOD}} {{/path}}` - {{描述}}

## 依赖安装

```bash
# 使用uv安装依赖（推荐）
uv sync

# 或者使用uv安装特定环境
uv pip install -e .

# 安装测试依赖
uv pip install -e ".[test]"
```

## 运行应用

```bash
# 开发环境启动
# 方法1：使用run_application.py（带热重载）
cd src/
python run_application.py

# 方法2：使用uvicorn命令
cd src/
uvicorn {{project_name}}.application:app --host 0.0.0.0 --port {{port}} --reload

# 生产环境启动
# 使用uvicorn启动（不带热重载）（workers制定线程数）
cd src/
uvicorn {{project_name}}.application:app --host 0.0.0.0 --port {{port}} --workers {{workers}}
```

## 运行测试

```bash
# 方法1：使用run_test.py运行测试
cd test/
python run_test.py

# 方法2：使用pytest命令运行测试
cd test/
pytest .

# 运行特定测试文件
cd test/
pytest {{project_name}}_test/application_test.py
```
