# Python 项目规则（Rules）

## 1. 项目结构规则

### 1.1 目录结构（禁止变更）

项目整体目录结构**统一在此处定义**，不得增加、删除、修改目录。

```
project-name/
├─ src/
│  └─ project_name/
│     ├─ api/
│     │  ├─ __init__.py
│     │  └─ *_api.py
│     ├─ service/
│     │  ├─ __init__.py
│     │  └─ *_service.py
│     ├─ client/
│     │  ├─ __init__.py
│     │  ├─ *_client.py
│     │  ├─ *_mysql_client.py
│     │  └─ *_mongo_client.py
│     ├─ config/
│     │  ├─ __init__.py
│     │  ├─ *_config.py
│     │  ├─ *_config_dev.py
│     │  └─ *_config_prod.py
│     ├─ model/
│     │  ├─ __init__.py
│     │  ├─ *_entity.py
│     │  ├─ *_mysql_entity.py
│     │  ├─ *_mongo_entity.py
│     │  ├─ *_dto.py
│     │  └─ *_vo.py
│     ├─ util/
│     │  ├─ __init__.py
│     │  └─ *_util.py
│     ├─ application.py
├─ tests/
│  └─ *_test.py
├─ docs/
├─ scripts/
├─ .gitignore
├─ pyproject.toml
├─ README.md
└─ rules.md
```

### 1.2 职责划分（必须遵守）

**api/**

- 接口层，仅负责：
    - 接口函数定义
    - 参数接收与校验
    - 调用 service 层
- ❌ 不允许定义类
- ❌ 不允许包含业务逻辑

**service/**

- 业务核心层
- 负责：
    - 业务规则
    - 业务编排
- ❌ 不允许直接访问外部资源

**client/**

- 外部访问层
- 负责：
    - 数据库访问（MySQL / MongoDB）
    - 第三方接口调用
- ❌ 不允许出现业务判断

**config/**

- 配置定义层
- 仅用于配置变量定义

**model/**

- 数据模型层
- 仅定义数据结构（Entity / DTO / VO）

**util/**

- 通用工具层
- 仅包含无状态工具函数

### 1.3. 命名规范（强制）

**api/**

- 文件名 **必须** 以 `_api.py` 结尾

```
user_api.py
order_api.py
```

**service/**

- 文件名 **必须** 以 `_service.py` 结尾

```
user_service.py
order_service.py
```

**client/**

- 文件名 **必须** 以 `_client.py` 结尾
- 数据库 client 需显式标识类型

```
user_client.py
user_mysql_client.py
user_mongo_client.py
```

**config/**

- 文件名规则：
    - 通用配置：`*_config.py`
    - 环境配置：`*_config_{env}.py`

```
db_config.py
db_config_dev.py
db_config_prod.py
```

**model/**

- 文件名 **必须** 以以下后缀之一结尾：
    - `_entity.py`
    - `_mysql_entity.py`
    - `_mongo_entity.py`
    - `_dto.py`
    - `_vo.py`

```
user_entity.py
user_mysql_entity.py
user_dto.py
user_vo.py
```

**util/**

- 文件名 **必须** 以 `_util.py` 结尾

```
time_util.py
string_util.py
```

**application.py**

- 用于：
    - 应用初始化
    - 依赖装配
    - 全局上下文管理
- ❌ 不允许编写具体业务逻辑

## 2. 代码编写规范（强制）

### 2.1 各层代码形式约束（强制）

**api/**

- 只能编写**接口函数**
- ❌ 不允许定义类

**service/**

- 每个文件必须先定义一个类
- 所有业务逻辑 **必须** 作为类的方法存在
- ❌ 不允许直接定义业务函数

**client/**

- 每个文件必须先定义一个类
- 所有外部访问逻辑 **必须** 作为类的方法存在

**util/**

- 只能编写工具函数
- ❌ 不允许定义类

**model/**

- 只能定义数据类（Entity / DTO / VO）
- ❌ 不允许包含任何业务逻辑或操作方法

**config/**

- 只能定义配置变量
- ❌ 不允许定义类
- ❌ 不允许定义函数

### 2.2 依赖与调用规则（强制）

- api 只能依赖 service
- service 只能依赖 client
- client 只能依赖第三方库 / 数据源

- api 之间 ❌ 不可相互依赖
- service 之间 ❌ 不可相互依赖
- client 之间 ❌ 不可相互依赖

- util 可被所有层调用
- config 仅用于读取配置

### 2.3 类方法调用规范（强制）

**公有方法（对外入口）**

- 可以：
    - 调用 **其它类的公有方法**
    - 调用 **当前类的私有方法**
- ❌ 不允许调用当前类的其它公有方法

**私有方法（内部逻辑封装）**

- 只能包含**单一、独立的业务逻辑**
- ❌ 不允许调用其它类的任何方法
- ❌ 不允许调用当前类的其它私有方法
- 目的：
    - 避免调用链过长
    - 保证逻辑可读、可拆解

**正确示例：**

```python
def fun_public():
    other.fun_public()
    _fun_private()
    return
```

**错误示例：**

```python
def _fun_private():
    fun_public_two()
    other.fun_public()
    _fun_private()
```

### 2.4 变量命名规范

**所有变量必须声明类型**
变量命名 = `语义 + 类型后缀`

```
*_list：list[int]
*_set：set[str]
*_dict：dict[int,str]
*_user_entity: UserEntity
*_user_entity_list: list[UserEntity]
```

**方法入参**

* 必须声明入参类型
* ❌ 禁止 `dict`
* ✅ 改为明确指定多个入参

**方法返回值**

* 必须声明返回值类型
* ❌ 禁止 `dict`
* ✅ 使用 **明确返回值**（tuple / DTO / VO）
    * ❌ 返回 `{}`
    * ✅ `return a, b` 或返回 DTO/VO

### 2.5 注释规范（强制）

* 注释 **必须** 使用 `#`
* ❌ 禁止使用 `"""` 或 `'''` 作为注释

**类注释**

* 每个类 **必须** 有注释
* 说明：类的职责与作用

**方法注释**

* 每个方法 **必须** 有注释
* 说明：方法的业务目的

## 3. 违规处理

* 不符合本规则的代码：
    * ❌ 不允许提交
    * ❌ 不允许合并

* Code Review 必须优先检查：
    * 目录结构
    * 命名规范
    * 依赖方向
    * 本章节代码规范