import logging
from datetime import datetime

from ..client.test_sql_client import TestSqlClient, get_test_sql_client
from ..model.test_sql_entity import TestSqlEntity

_log = logging.getLogger(__name__)


# 测试服务类
class TestService:
    # 注入测试实体数据库操作类
    def __init__(self, test_sql_client: TestSqlClient):
        self._test_sql_client = test_sql_client

    # 根据ID查询，如果不存在则创建一个新的项目
    def get_or_create_item(self, item_id: int, name: str, description: str) -> TestSqlEntity:
        # 先查询是否存在
        entity = self._test_sql_client.get_by_id(item_id)
        # 如果不存在，则创建新的实体
        if entity is None:
            # 创建并存储新的实体
            new_entity = TestSqlEntity(id=item_id, name=name, description=description,
                                       created_at=datetime.now(), updated_at=datetime.now())
            saved = self._test_sql_client.insert_by_id(new_entity)
            if not saved:
                raise Exception("Failed to save entity")
            # 再次查询返回最新数据
            entity = self._test_sql_client.get_by_id(item_id)
        # 返回实体
        if entity is None:
            raise Exception("Failed to find entity after creation")
        return entity


# 创建测试实体数据库操作类实例
_log.info("Creating test service")
_test_service = TestService(get_test_sql_client())


# 获取测试服务类实例
def get_test_service() -> TestService:
    return _test_service
