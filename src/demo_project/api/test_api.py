from fastapi import APIRouter, Depends

from demo_project.model.api_response import ApiResponse
from demo_project.model.test_dto import TestDTO
from demo_project.model.test_sql_entity import TestSqlEntity
from demo_project.model.test_vo import TestVO
from demo_project.service.test_service import TestService, get_test_service

router = APIRouter()


# 根据ID获取或创建项目
@router.post("/test")
def get_or_create_item(
        dto: TestDTO,
        test_service: TestService = Depends(get_test_service)
) -> ApiResponse[TestVO]:
    entity: TestSqlEntity = test_service.get_or_create_item(dto.item_id, dto.name, dto.description)
    vo: TestVO = TestVO(entity.id, entity.name, entity.description)
    return ApiResponse(data=vo)
