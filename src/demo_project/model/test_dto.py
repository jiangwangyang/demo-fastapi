from pydantic import BaseModel, field_validator


# 测试接口入参 DTO
# 所属接口：POST /demo/test
# 数据来源：前端请求
class TestDTO(BaseModel):
    # 主键
    id: int
    # 测试名称
    name: str
    # 测试描述
    description: str

    @field_validator("id")
    @classmethod
    def validate_id(cls, id):
        if id <= 0:
            raise ValueError("id must be positive")
        return id
