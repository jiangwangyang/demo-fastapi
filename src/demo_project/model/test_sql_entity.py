from dataclasses import dataclass
from datetime import datetime


# 测试数据库实体
@dataclass
class TestSqlEntity:
    # 主键
    id: int
    # 测试名称
    name: str
    # 测试描述
    description: str
    # 创建时间
    created_at: datetime
    # 更新时间
    updated_at: datetime
