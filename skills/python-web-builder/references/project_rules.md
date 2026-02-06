# 项目结构规则

## 目录结构（禁止变更）

```
demo-fastapi-master/
├─ src/
│  ├─ demo_project/
│  │  ├─ api/
│  │  │  ├─ __init__.py
│  │  │  └─ *_api.py
│  │  ├─ service/
│  │  │  ├─ __init__.py
│  │  │  └─ *_service.py
│  │  ├─ client/
│  │  │  ├─ __init__.py
│  │  │  └─ *_client.py | *_sql_client.py | *_mongo_client.py
│  │  ├─ config/
│  │  │  ├─ __init__.py
│  │  │  ├─ config.py
│  │  │  ├─ config_dev.py
│  │  │  └─ config_prod.py
│  │  ├─ model/
│  │  │  ├─ __init__.py
│  │  │  ├─ *_entity.py | *_sql_entity.py | *_mongo_entity.py
│  │  │  ├─ *_dto.py
│  │  │  └─ *_vo.py
│  │  ├─ util/
│  │  │  ├─ __init__.py
│  │  │  └─ *_util.py
│  │  ├─ application.py
│  │  └─ __init__.py
│  └─ run_application.py
├─ test/
│  ├─ demo_project_test/
│  │  ├─ __init__.py
│  │  └─ *_test.py
│  └─ run_test.py
├─ skills/
├─ docs/
├─ README.md
├─ AGENTS.md
├─ rules.md
├─ pyproject.toml
├─ uv.lock
└─ .gitignore
```

## api/

- 接口层
- 负责接口函数定义
- 负责参数接收与校验
- 负责调用 service 层
- 禁止定义类
- 禁止包含业务逻辑

## service/

- 业务核心层
- 负责业务规则
- 负责业务编排
- 禁止直接访问外部资源

## client/

- 外部访问层
- 负责数据库访问（SQL / MongoDB 等）
- 负责第三方接口调用
- 禁止出现业务判断

## config/

- 配置定义层
- 仅用于配置变量定义

## model/

- 数据模型层
- 仅定义数据结构（Entity / DTO / VO）

## util/

- 通用工具层
- 仅包含无状态工具函数

## 其他目录

- test/：测试用例与测试入口
- skills/：本地技能与参考资料（不参与业务代码）
