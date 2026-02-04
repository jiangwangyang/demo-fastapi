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