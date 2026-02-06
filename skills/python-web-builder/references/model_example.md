```python
# src/demo_project/model/api_response.py
# 测试展示实体
from typing import Any, TypeVar, Generic

from pydantic import BaseModel

# 声明泛型类型变量T，作为data字段的类型占位符
T = TypeVar("T")


# Api通用响应实体类，继承Generic[T]，成为泛型数据类，T绑定到data字段的类型
class ApiResponse(BaseModel, Generic[T]):
    # 是否成功
    success: bool = True
    # 消息
    message: str = "success"
    # 数据
    data: T | None = None
    # 附加信息
    extra: Any = None

# src/demo_project/model/demo_dto.py
from pydantic import BaseModel, field_validator


# 演示接口入参 DTO
# 所属接口：POST /demo/test
# 数据来源：前端请求
class DemoDTO(BaseModel):
    # 主键
    id: int
    # 演示名称
    name: str
    # 演示描述
    description: str

    @field_validator("id")
    @classmethod
    def validate_id(cls, id):
        if id <= 0:
            raise ValueError("id must be positive")
        return id

# src/demo_project/model/demo_sql_entity.py
from dataclasses import dataclass
from datetime import datetime


# 演示数据库实体
@dataclass
class DemoSqlEntity:
    # 主键
    id: int
    # 演示名称
    name: str
    # 演示描述
    description: str
    # 创建时间
    created_at: datetime
    # 更新时间
    updated_at: datetime

# src/demo_project/model/demo_vo.py
from dataclasses import dataclass


# 演示展示实体
@dataclass
class DemoVO:
    # 主键
    id: int
    # 演示名称
    name: str
    # 演示描述
    description: str
```
