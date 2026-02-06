# client 代码编写规范

## 定位说明
- client 层是**外部访问层**，仅负责与**数据库 / 第三方系统 / 外部资源**交互。
- client **不关心业务含义、不做业务判断、不参与业务编排**。

## 文件命名规范

- 文件名 **必须** 以 `_client.py` 结尾。
- 数据库 client **必须显式标识数据库类型**（如 `user_mysql_client.py`, `user_mongo_client.py`）。
- **禁止** 使用模糊命名（如 `user.py`, `userDao.py`, `user_repository.py`）。

## 类命名与定义规范

- 每个 client 文件 **必须** 定义且 **只能** 定义一个 client 类。
- 类名 **必须** 采用 **PascalCase** 格式。
- 类名含义 **必须** 明确，体现访问对象（如 `UserMysqlClient`）。
- 每个 client 类 **必须** 编写类注释，说明访问的外部资源及数据来源类型。类注释 **必须** 使用 `#` 符号并写在类定义正上方，**禁止** 使用 `"""` 或 `'''`。

## 变量命名与定义规范

- 所有变量 **必须** 声明类型。
- 变量命名 **必须** 符合 `语义 + 类型后缀` 格式（如 `user_id: int`, `user_entity: UserEntity`）。
- `dict` 类型变量（如 `result_row_dict`） **仅限** 在方法内部使用，**禁止** 作为方法入参或返回值。

## 方法命名与定义规范

- 方法命名 **必须** 使用 **动词 + 名词** 格式，明确外部访问动作（如 `get_user_by_id`）。
- 方法命名 **禁止** 出现业务语义词（如 `check`, `decide`, `process`, `handle`）。
- 方法入参 **必须** 显式声明类型，**禁止** 使用 `dict` 作为入参，**禁止** 使用“万能参数对象”。
- 方法返回值 **必须** 显式声明类型，返回值 **必须** 是 Entity、Entity List、基础类型（int/bool/str）或含义明确的 tuple，**禁止** 返回 `dict` 类型数据。
- 如果方法入参和返回值可以为None，**必须** 显示声明类型为 `类型 | None`（如 `int | None`, `UserEntity | None`）。
- 每个方法 **必须** 编写注释，说明外部访问目的及返回数据含义。方法注释 **必须** 使用 `#` 符号并写在方法定义正上方，**禁止** 使用 `"""` 或 `'''`。

## 业务逻辑规范

- client 层 **必须** 只负责外部访问与数据映射。
- client 层 **严禁（禁止）** 出现任何业务判断或逻辑处理（如根据状态抛出业务异常）。
- 公有方法 **必须** 仅用于 service 层调用。
- 公有方法 **可以** 调用当前类的私有方法。
- 公有方法 **禁止** 调用其他 client、service 的公有方法。
- 私有方法 **必须** 满足单一职责，仅封装单一外部访问动作。
- 私有方法 **禁止** 调用其他 client、service 或当前类的其他私有方法。

## 注释形式规范

- 每个 client 类 **必须** 包含注释，注释内容 **必须** 明确说明该 client 访问的外部资源名称及数据来源类型。
- 每个方法（包括公有和私有方法） **必须** 包含注释，注释内容 **必须** 明确说明外部访问的具体目的以及返回数据的具体含义。
- 注释内容 **必须** 写在类定义或方法定义的正上方。
- 注释 **必须** 使用 `#` 符号。
- **禁止** 使用 `"""` 或 `'''`（文档字符串）进行注释。

## 日志记录规范

- client 文件 **必须** 使用 `__name__` 定义模块级 logger，且日志操作对象 **必须** 命名为 `_log`。
- 日志 **仅限** 用于记录实例创建及外部资源连接信息。
- **禁止** 在 client 层记录业务状态或业务处理结果。

## 实例创建规范

- client 类 **必须** 只负责定义访问行为。
- client 实例的创建 **必须** 在模块内完成，且实例变量 **必须** 定义为私有（以下划线开头）。
- **必须** 通过 `get_xxx_client` 方法对外提供实例。
- **禁止** 在外部直接调用类构造函数（如 `TestSqlClient()`）创建实例。

## 标准示例

```python
import logging
from datetime import datetime
from typing import List

from project_name.config.config import DATABASE_URL, DATABASE_USERNAME, DATABASE_PASSWORD
from project_name.model.test_sql_entity import TestSqlEntity

_log = logging.getLogger(__name__)

# 测试实体 MySQL 数据访问客户端
class TestSqlClient:
    # 初始化数据库连接信息
    def __init__(self, url: str, username: str, password: str):
        self.url = url
        self.username = username
        self.password = password
        self._storage = {}

    # 查询所有测试实体
    def get_all(self) -> List[TestSqlEntity]:
        return list(self._storage.values())

    # 根据ID查询测试实体
    def get_by_id(self, entity_id: int) -> TestSqlEntity | None:
        return self._storage.get(entity_id)

    # 插入测试实体
    def insert_by_id(self, entity: TestSqlEntity) -> bool:
        self._storage[entity.id] = entity
        return True

# 创建测试实体数据库客户端实例
_log.info("Creating TestSqlClient")
_test_sql_client = TestSqlClient(DATABASE_URL, DATABASE_USERNAME, DATABASE_PASSWORD)

# 获取测试实体数据库客户端实例
def get_test_sql_client() -> TestSqlClient:
    return _test_sql_client
```
