# 实体类编写规范

## 定位说明

- **DTO (Data Transfer Object)**：外部访问层入参，负责与**外部请求/第三方系统**的原始数据对接，属于**不可信数据边界**。
- **Entity (Business Entity)**：内部领域模型，负责在 **service / client** 之间流转，属于**可信业务数据**。
- **VO (View Object)**：外部访问层出参，负责向**前端或调用方**展示数据，属于**格式化展示数据**。

## 文件命名规范

- 文件名 **必须** 以对应的后缀结尾：
- DTO：`*_dto.py`（如 `user_create_dto.py`）
- Entity：`*_entity.py`（如 `user_entity.py`）
- VO：`*_vo.py`（如 `user_info_vo.py`）

## 类命名与定义规范

- **必须** 一个文件定义且 **只能** 定义一个类。
- 文件名 **必须** 与类名语义一一对应，采用 **小写 + 下划线** 格式。
- 类名 **必须** 采用 **PascalCase** 格式。
- 类名后缀 **必须** 与文件后缀一致（`UserCreateDTO`, `UserEntity`, `UserInfoVO`）。
- 类定义框架要求：
- **DTO**：**必须** 继承 `pydantic.BaseModel`。
- **Entity / VO**：**必须** 使用 `@dataclass` 装饰器，且 **禁止** 继承任何父类。
- 每个类 **必须** 编写类注释，说明其用途、所属接口或对应数据库。类注释 **必须** 使用 `#` 符号并写在类定义正上方，**禁止** 使用 `"""` 或 `'''`。

## 变量命名与定义规范

- 所有变量 **必须** 声明类型。
- 变量命名 **必须** 符合 `语义 + 类型后缀` 格式（如 `user_id: int`, `create_time_str: str`）。
- **每个属性必须有注释**，说明该字段的业务含义。注释 **必须** 使用 `#` 符号并写在变量定义正上方。
- **DTO** 中 **必须** 包含字段校验逻辑（使用 `@field_validator`），且只能包含校验逻辑。

## 方法命名与定义规范

- **DTO**：除校验方法（`@field_validator`）外，**禁止** 定义任何其他方法。
- **Entity / VO**：**禁止** 定义任何方法（包括计算、转换、判断方法）。
- 类中 **禁止** 出现业务语义词（如 `check`, `process`, `handle`）。

## 业务逻辑规范

- 实体类层 **严禁（禁止）** 出现任何业务判断或逻辑处理。
- **禁止** 在实体类中操作数据库、调用 service、client 或第三方接口。
- **禁止** 在 Entity / VO 中编写任何校验逻辑（校验职责由 DTO 承担）。
- 对象之间的转换逻辑 **必须** 剥离至独立的转换层，实体类本身保持纯净的数据结构。

## 注释形式规范

- 每一个类和每一个变量 **必须** 包含注释。
- 注释内容 **必须** 写在定义对象的正上方。
- 注释 **必须** 使用 `#` 符号。
- **禁止** 使用 `"""` 或 `'''`（文档字符串）进行注释。

## 日志记录规范

- 实体类文件 **通常不定义** logger。
- **禁止** 在属性校验或初始化过程中打印业务状态日志。

## 实例创建规范

- **DTO**：通常由框架（如 FastAPI）根据请求自动实例化。
- **Entity / VO**：由 service 层或 assembler 转换层手动实例化。
- 变量赋值 **必须** 严格遵守类型声明。

## 标准示例

### DTO 示例

```python
from pydantic import BaseModel, field_validator

# 用户创建接口入参 DTO
# 所属接口：POST /api/user/create
# 数据来源：前端请求
class UserCreateDTO(BaseModel):
    # 用户姓名
    user_name: str
    # 用户年龄（必须为正整数）
    user_age_int: int

    @field_validator("user_age_int")
    @classmethod
    def age_must_be_positive(cls, v: int) -> int:
        # 校验年龄是否为正数
        if v <= 0:
            raise ValueError("age must be positive")
        return v

```

### Entity 示例

```python
from dataclasses import dataclass

# 用户业务实体
# 对应数据库表：user_info
@dataclass
class UserEntity:
    # 用户唯一标识
    user_id: int
    # 用户姓名
    user_name: str
    # 用户年龄
    user_age_int: int

```

### VO 示例

```python
from dataclasses import dataclass

# 用户信息展示对象
# 用于前端详情页面展示
@dataclass
class UserInfoVO:
    # 格式化后的用户唯一标识
    user_id_str: str
    # 用户脱敏姓名
    display_name_str: str

```
