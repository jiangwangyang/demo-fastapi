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