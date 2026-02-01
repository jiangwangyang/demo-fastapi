import logging
from datetime import datetime
from typing import Optional, List

from ..config.config import DATABASE_URL, DATABASE_USERNAME, DATABASE_PASSWORD
from ..model.test_sql_entity import TestSqlEntity

_log = logging.getLogger(__name__)


# 测试实体数据库操作类
# 模拟数据库存储
class TestSqlClient:
    # 初始化一些示例数据
    def __init__(self, url: str, username: str, password: str):
        self.url = url
        self.username = username
        self.password = password
        self._storage = {
            1: TestSqlEntity(id=1, name="Example Item 1", description="This is an example item",
                             created_at=datetime.now(), updated_at=datetime.now()),
            2: TestSqlEntity(id=2, name="Example Item 2", description="This is another example item",
                             created_at=datetime.now(), updated_at=datetime.now())
        }

    # 获取所有实体
    def get_all(self) -> List[TestSqlEntity]:
        return list(self._storage.values())

    # 根据ID获取实体
    def get_by_id(self, entity_id: int) -> Optional[TestSqlEntity]:
        return self._storage.get(entity_id)

    # 根据ID保存实体
    def insert_by_id(self, entity: TestSqlEntity) -> bool:
        if not entity.id or entity.id in self._storage:
            return False
        self._storage[entity.id] = entity
        return True

    # 根据ID更新实体
    def update_by_id(self, entity: TestSqlEntity) -> bool:
        if entity.id in self._storage:
            self._storage[entity.id] = entity
            return True
        return False

    # 根据ID删除实体
    def delete_by_id(self, entity_id: int) -> bool:
        if entity_id in self._storage:
            del self._storage[entity_id]
            return True
        return False


# 创建测试实体数据库操作类实例
_log.info("Creating test sql client")
_log.info("Using database url: %s", DATABASE_URL)
_log.info("Using database username: %s", DATABASE_USERNAME)
_log.info("Using database password: %s", DATABASE_PASSWORD)
_test_sql_client = TestSqlClient(DATABASE_URL, DATABASE_USERNAME, DATABASE_PASSWORD)


# 获取测试实体数据库操作类实例
def get_test_sql_client() -> TestSqlClient:
    return _test_sql_client
