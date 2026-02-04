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