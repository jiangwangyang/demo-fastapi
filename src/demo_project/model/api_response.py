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
