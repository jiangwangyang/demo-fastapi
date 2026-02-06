```python
# src/demo_project/service/demo_service.py
import logging
from datetime import datetime

from demo_project.client.demo_sql_client import DemoSqlClient
from demo_project.model.demo_sql_entity import DemoSqlEntity

_log = logging.getLogger(__name__)


# 演示服务类
class DemoService:
    # 注入演示实体数据库操作类
    def __init__(self, demo_sql_client: DemoSqlClient):
        self._demo_sql_client = demo_sql_client

    # 根据ID查询，如果不存在则创建一个新的项目
    def get_or_create_item(self, item_id: int, name: str, description: str) -> DemoSqlEntity:
        # 先查询是否存在
        entity = self._demo_sql_client.get_by_id(item_id)
        # 如果不存在，则创建新的实体
        if entity is None:
            # 创建并存储新的实体
            new_entity = DemoSqlEntity(id=item_id, name=name, description=description,
                                       created_at=datetime.now(), updated_at=datetime.now())
            saved = self._demo_sql_client.insert_by_id(new_entity)
            if not saved:
                raise Exception("Failed to save entity")
            # 再次查询返回最新数据
            entity = self._demo_sql_client.get_by_id(item_id)
        # 返回实体
        if entity is None:
            raise Exception("Failed to find entity after creation")
        return entity


# 演示实体数据库操作类实例
_demo_service: DemoService | None = None


# 创建演示服务类实例
def create_demo_service(demo_sql_client: DemoSqlClient) -> DemoService:
    global _demo_service
    _demo_service = DemoService(demo_sql_client)
    return _demo_service


# 获取演示服务类实例
def get_demo_service() -> DemoService:
    if _demo_service is None:
        raise RuntimeError("DemoService has not been created")
    return _demo_service
```
