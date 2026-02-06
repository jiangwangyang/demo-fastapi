import logging

from fastapi import APIRouter, Depends

from demo_project.model.api_response import ApiResponse
from demo_project.model.demo_dto import DemoDTO
from demo_project.model.demo_sql_entity import DemoSqlEntity
from demo_project.model.demo_vo import DemoVO
from demo_project.service.demo_service import DemoService, get_demo_service

_log = logging.getLogger(__name__)
router = APIRouter()


# 根据ID获取或创建项目
@router.post("/demo")
def get_or_create_item(
        dto: DemoDTO,
        demo_service: DemoService = Depends(get_demo_service)
) -> ApiResponse[DemoVO]:
    # 调用服务层方法获取或创建实例
    entity: DemoSqlEntity = demo_service.get_or_create_item(dto.id, dto.name, dto.description)
    # 将实体对象转换为响应对象
    vo: DemoVO = DemoVO(entity.id, entity.name, entity.description)
    # 返回API响应
    return ApiResponse(data=vo)


# 测试异常接口
@router.post("/error")
def error():
    raise RuntimeError("This is a demo error")
