# 项目结构规则

## 目录结构

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

## 目录规范

- `api/` 接口层，定义接口函数、接收/校验参数、调用 service；禁止定义类与业务逻辑。
- `service/` 业务逻辑层，负责业务规则与编排；禁止直接访问外部资源。
- `client/` 外部访问层，负责数据库与第三方接口访问；禁止业务判断。
- `config/` 配置定义层，仅用于配置变量定义。
- `model/` 数据模型层，仅定义数据结构（Entity / DTO / VO）。
- `util/` 通用工具层，仅包含无状态工具函数。
- `test/` 测试用例与测试入口。
- `skills/` 本地技能与参考资料（不参与业务代码）。

## 文件规范

- api 文件名必须以 `_api.py` 结尾，禁止模糊命名（如 `user.py`, `user_controller.py`, `user_router.py`）。
- service 文件名必须以 `_service.py` 结尾，置于 `src/demo_project/service/`，禁止缩写或模糊命名。
- client 文件名必须以 `_client.py` 结尾，数据库 client 必须显式标识数据库类型（如 `user_mysql_client.py`, `user_mongo_client.py`），禁止 `user.py`, `userDao.py`, `user_repository.py`。
- config 仅允许在 `src/demo_project/config/` 维护；入口为 `config.py`，环境文件为 `config_dev.py`、`config_prod.py`。
- model 文件名必须以 `_dto.py` / `_entity.py` / `_vo.py` 结尾，对应 DTO/Entity/VO。
- util 文件名必须以 `_util.py` 结尾，名称明确用途（如 `time_util.py`）；禁止 `utils.py`, `common.py`, `helper.py`, `tool.py`。
- application 入口文件必须为 `src/demo_project/application.py`。
- test 入口为 `test/run_test.py`，用例在 `test/demo_project_test/`，文件名以 `_test.py` 结尾且必须显式导入被测模块，禁止动态导入。

## 变量规范

- 所有变量必须显式声明类型，命名遵循 `语义 + 类型后缀`（如 `user_dto: UserDTO`, `trace_id: str`）。
- config 变量名必须为全大写 + 下划线（如 `DATABASE_URL`），只允许纯配置值，不允许业务计算。
- 禁止在 api/service/client/util/test 方法入参或返回值使用 `dict`；`dict` 仅允许在 client/util 方法内部使用。
- 若入参或返回值可为空，必须使用 `类型 | None` 显式声明。

## 类规范

- api/util/config 层禁止定义类；util 禁止全局可变变量。
- client/service 层每文件且仅一个类，类名使用 PascalCase，语义明确；类注释必须用 `#` 写在类定义上方。
- model 每文件且仅一个类，类名 PascalCase，类名后缀与文件后缀一致；类注释必须用 `#` 写在类定义上方。
- DTO 必须继承 `pydantic.BaseModel`；Entity/VO 必须使用 `@dataclass`，禁止继承父类。

## 方法规范

- api 仅允许顶层函数，每个接口函数必须使用 `@router` 注解；命名为动词+名词，禁止实现细节命名。
- api 入参必须显式类型且 Body 参数必须为 DTO；返回值必须为 `ApiResponse` 且显式标注类型。
- service 公有方法为动词+业务语义，私有方法以下划线开头；禁止“万能参数对象”，返回值为 DTO/VO/Entity/基础类型/明确 tuple。
- client 方法命名为动词+名词，禁止业务语义词（如 `check`, `decide`, `process`, `handle`）；返回值为 Entity/Entity List/基础类型/明确 tuple。
- util 函数命名为动词+名词，禁止业务语义词；禁止可变默认参数（如 `[]`, `{}`），返回值为基础类型或明确 tuple。
- DTO 仅允许 `@field_validator` 校验方法；Entity/VO 禁止定义任何方法。
- model 类内禁止出现业务语义词（如 `check`, `process`, `handle`）。

## 代码规范

- api 仅做请求分发与响应封装；禁止业务逻辑、业务异常、类定义、私有业务函数；接口之间禁止互相调用，禁止直接调用 client。
- api 必须通过 `Depends` 注入 service 且变量显式类型；禁止手动实例化 service；路由实例必须在模块内创建且变量名为 `router`，禁止创建任何其它实例；api 文件仅作为路由挂载点，`include_router` 在应用启动入口完成。
- api 接口函数仅可调用 service 层公有方法。
- service 仅依赖 client/model/util/config，严禁依赖 api 或其他 service；禁止直接访问数据库或第三方接口。
- service 实例必须在模块内创建、私有变量持有，通过 `get_xxx_service` 对外提供；必须通过构造函数注入 client。
- service 公有方法可调用私有方法与注入 client 公有方法；公有方法禁止互调、禁止调用其他 service；私有方法单一职责，禁止调用其他方法或其他类。
- client 只负责外部访问与数据映射，严禁业务判断；公有方法仅供 service 调用，可调用当前类私有方法；公有方法禁止调用其他 client/service。
- client 私有方法单一职责，禁止调用其他 client/service 或当前类其他私有方法；实例必须在模块内创建且私有变量持有，通过 `get_xxx_client` 提供，禁止外部直接构造。
- config 层只定义变量，禁止类与函数：`config.py` 读取环境并动态导入环境配置，仅用标准库；环境文件只定义变量，不做计算/导入/环境读取；业务代码只能 `from demo_project.config import config`。
- 环境配置文件变量名必须与 `config.py` 声明一致且拼写准确（如 `DATABASE_URL`）。
- model 层严禁业务逻辑、数据库/服务/第三方调用；校验仅在 DTO；对象转换必须独立于实体类。
- DTO 通常由框架自动实例化；Entity/VO 由 service 或转换层手动实例化，赋值必须严格符合类型声明。
- util 层必须无状态，仅纯计算/格式转换/通用校验；禁止数据库/网络/IO，禁止调用 client/service/api/config，禁止 util 之间互调；禁止任何实例创建逻辑；可被所有层级调用。
- application 仅做应用初始化、依赖装配、全局上下文管理；必须提供 `create_app()`，并暴露 `app: FastAPI`；只从 api 层挂载路由，可加载 service/client 做启动初始化但禁止业务流程。
- application 必须统一注册全局异常处理器，响应使用统一模型（如 `ApiResponse`），处理器仅记录日志与构造响应。
- test 使用 `TestClient`，统一从 `demo_project.application` 导入 `app`；断言覆盖状态码与响应体结构；测试函数按“准备输入输出→调用→断言”顺序组织，独立可复现；禁止使用二级列表。

## 注释规范

- 所有类、方法/函数、类属性必须有注释，内容清晰说明职责/用途/字段含义。
- 注释必须使用 `#` 且写在定义正上方，禁止使用 `"""` 或 `'''`。

## 日志规范

- api/client/service/util/application 必须使用 `__name__` 创建模块级 logger，变量名统一为 `_log`。
- api 日志仅记录接口调用与响应信息，禁止记录业务状态或处理结果。
- client 日志仅记录实例创建与外部资源连接信息，禁止记录业务状态或结果。
- service 日志允许记录关键业务流程触发、业务异常与重要状态变更。
- util 日志仅用于少量关键异常，禁止频繁打印或记录业务状态。
- application 启动过程关键节点必须记录日志。
- model 通常不定义 logger，禁止在校验或初始化中打印业务状态日志。
