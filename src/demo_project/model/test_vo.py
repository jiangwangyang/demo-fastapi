from dataclasses import dataclass


# 测试展示实体
@dataclass
class TestVO:
    # 主键
    id: int
    # 测试名称
    name: str
    # 测试描述
    description: str
