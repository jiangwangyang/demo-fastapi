```python
# src/demo_project/client/demo_sql_client.py
import logging
from datetime import datetime
from typing import List

from demo_project.model.demo_sql_entity import DemoSqlEntity

_log = logging.getLogger(__name__)


# 演示实体数据库操作类
# 模拟数据库存储
class DemoSqlClient:
    # 初始化一些示例数据
    def __init__(self, url: str, username: str, password: str):
        self.url = url
        self.username = username
        self.password = password
        self._storage = {
            1: DemoSqlEntity(id=1, name="Example Item 1", description="This is an example item",
                             created_at=datetime.now(), updated_at=datetime.now()),
            2: DemoSqlEntity(id=2, name="Example Item 2", description="This is another example item",
                             created_at=datetime.now(), updated_at=datetime.now())
        }

    # 获取所有实体
    def get_all(self) -> List[DemoSqlEntity]:
        return list(self._storage.values())

    # 根据ID获取实体
    def get_by_id(self, entity_id: int) -> DemoSqlEntity | None:
        return self._storage.get(entity_id)

    # 根据ID保存实体
    def insert_by_id(self, entity: DemoSqlEntity) -> bool:
        if not entity.id or entity.id in self._storage:
            return False
        self._storage[entity.id] = entity
        return True

    # 根据ID更新实体
    def update_by_id(self, entity: DemoSqlEntity) -> bool:
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


# 演示实体数据库操作类实例
_demo_sql_client: DemoSqlClient | None = None


# 创建演示实体数据库操作类实例
def create_demo_sql_client(url: str, username: str, password: str) -> DemoSqlClient:
    global _demo_sql_client
    _demo_sql_client = DemoSqlClient(url, username, password)
    return _demo_sql_client


# 获取演示实体数据库操作类实例
def get_demo_sql_client() -> DemoSqlClient:
    if _demo_sql_client is None:
        raise RuntimeError("DemoSqlClient has not been created")
    return _demo_sql_client
```
