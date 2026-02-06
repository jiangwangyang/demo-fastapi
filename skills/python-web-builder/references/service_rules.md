# service 代码编写规范

## 定位说明

- service 层是**业务逻辑层**，负责承载完整的业务能力、业务规则判断及流程编排。
- service **仅依赖** client, model, util, config，**严禁**依赖 api 或与其他 service 相互依赖。
- service **禁止**直接操作数据库或第三方接口，必须通过 client 层进行资源访问。

## 文件命名规范

- 文件名 **必须** 以 `_service.py` 结尾（如 `user_service.py`, `order_service.py`）。
- 文件 **必须** 存放于项目约定的 service 目录中（如 `src/project_name/service/`）。
- **禁止** 使用缩写或模糊命名。

## 类命名与定义规范

- 每个 service 文件 **必须** 定义且 **只能** 定义一个 service 类。
- 类名 **必须** 采用 **PascalCase** 格式（如 `UserService`）。
- 类名 **必须** 与文件名语义保持一致。
- 每个 service 类 **必须** 编写类注释，说明其负责的业务职责。类注释 **必须** 使用 `#` 符号并写在类定义正上方，**禁止** 使用 `"""` 或 `'''`。

## 变量命名与定义规范

- 所有变量（包括成员变量与局部变量） **必须** 声明类型。
- 变量命名 **必须** 符合 `语义 + 类型后缀` 格式（如 `user_id_int: int`, `order_entity_list: list[OrderEntity]`）。
- 成员变量（如注入的 client） **必须** 定义为私有，以下划线开头。

## 方法命名与定义规范

- **公有方法**：作为对外业务入口，使用 **动词 + 业务语义** 命名（如 `register_new_user`）。
- **私有方法**：仅用于内部逻辑拆分，方法名 **必须** 以单下划线 `_` 开头。
- 方法入参 **必须** 显式声明类型，**禁止** 使用 `dict` 作为入参，**禁止** 使用“万能参数对象”。
- 方法返回值 **必须** 显式声明类型，返回值 **必须** 是 DTO、VO、Entity、基础类型或明确的 tuple，**禁止** 返回 `dict` 或空字典 `{}`。
- 如果入参或返回值可为空，**必须** 显式声明为 `类型 | None`。
- 每个方法 **必须** 编写注释，说明业务目的。方法注释 **必须** 使用 `#` 符号并写在方法定义正上方，**禁止** 使用 `"""` 或 `'''`。

## 业务逻辑规范

- 公有方法 **可以** 调用当前类的私有方法。
- 公有方法 **可以** 调用注入的 client 类的公有方法。
- 公有方法 **禁止** 调用当前类的其他公有方法。
- 公有方法 **禁止** 调用其他 service 类的任何方法。
- 私有方法 **必须** 满足单一职责，仅封装单一、独立的业务逻辑。
- 私有方法 **禁止** 调用其他类的任何方法（包括 client）。
- 私有方法 **禁止** 调用当前类的其他私有方法或公有方法。

## 注释形式规范

- 每个类及方法（公有/私有） **必须** 包含注释。
- 注释内容 **必须** 明确说明业务职责（类）或业务目的（方法）。
- 注释内容 **必须** 写在类定义或方法定义的正上方。
- 注释 **必须** 使用 `#` 符号，**禁止** 使用 `"""` 或 `'''`。

## 日志记录规范

- service 文件 **必须** 使用 `__name__` 定义模块级 logger，且日志操作对象 **必须** 命名为 `_log`。
- 日志 **允许** 记录关键业务流程的触发、业务异常信息及重要的状态变更。

## 实例创建规范

- service 类 **必须** 通过构造函数 `__init__` 注入所需的 client 实例。
- **禁止** 在 service 方法内部直接实例化 client 类。
- service 实例的创建 **必须** 在模块内完成，且实例变量 **必须** 定义为私有（以下划线开头）。
- **必须** 通过 `get_xxx_service` 方法对外提供实例。
- **禁止** 在外部直接调用类构造函数（如 `UserService()`）创建实例。

## 标准示例

```python
from project_name.client.user_client import UserClient
from project_name.model.user_entity import UserEntity
from project_name.model.user_vo import UserVO

# 用户业务服务，负责用户创建与查询相关核心业务逻辑
class UserService:
    def __init__(self, user_client: UserClient):
        # 用户数据访问 client
        self._user_client = user_client

    # 创建用户的业务入口
    def create_user(self, name_str: str, age_int: int) -> UserVO:
        # 校验年龄合法性
        self._validate_age(age_int)

        # 构建用户实体
        user_entity: UserEntity = UserEntity(
            name_str=name_str,
            age_int=age_int
        )

        # 保存用户信息
        saved_user_entity: UserEntity = self._user_client.save(user_entity)

        # 构建返回 VO
        user_vo: UserVO = UserVO(
            user_id_int=saved_user_entity.user_id_int,
            name_str=saved_user_entity.name_str
        )
        return user_vo

    # 校验用户年龄是否合法
    def _validate_age(self, age_int: int) -> None:
        if age_int <= 0:
            raise ValueError("age must be greater than 0")
```
