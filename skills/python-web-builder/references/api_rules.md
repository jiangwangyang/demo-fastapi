# api 代码编写规范

## 定位说明

- api 层是**接口层 / 接入层**，仅负责与**前端 / 外部系统**的通信协议交互。
- api 负责：**接口定义、参数接收、参数校验、调用 service 层**。
- api **不包含任何业务逻辑、不定义类、不参与业务编排**。

## 文件命名规范

- 文件名 **必须** 以 `_api.py` 结尾。
- **禁止** 使用模糊命名（如 `user.py`, `user_controller.py`, `user_router.py`）。

## 类命名与定义规范

- util 层 **禁止** 定义类。
- 所有功能 **必须** 以顶层函数（Function）的形式实现。
- 每个顶层函数（Function）上 **必须** 添加 `@router` 注解以声明为 Api 接口。

## 变量命名与定义规范

- 所有变量 **必须** 声明类型。
- 变量命名 **必须** 符合 `语义 + 类型后缀` 格式（如 `user_dto: UserDTO`, `trace_id: str`）。
- **禁止** 使用 `dict` 类型变量接收或处理业务数据。

## 方法命名与定义规范

- 方法命名 **必须** 使用 **动词 + 名词** 格式，明确接口动作（如 `create_user`, `get_user_by_id`）。
- 方法命名 **禁止** 出现实现细节词（如 `call_service`, `process_logic`, `handle_request`）。
- 方法入参 **必须** 显式声明类型，且 **必须** 使用 DTO 对象作为 Body 参数，**禁止** 使用 `dict` 或零散的业务字段。
- 方法返回值 **必须** 显式声明类型，且 **统一** 返回 `ApiResponse` 对象，**禁止** 返回 `dict` 或 Entity。
- 每个方法 **必须** 编写注释，说明接口用途及行为。方法注释 **必须** 使用 `#` 符号并写在方法定义正上方，**禁止** 使用 `"""` 或 `'''`。

## 业务逻辑规范

- api 文件 **只能** 包含接口函数定义，**禁止** 在 api 文件内定义任何类（Class）。
- 每个接口函数 **必须** 作为独立入口，**禁止** 在 api 层定义辅助性质的业务私有函数。
- api 层 **必须** 只负责请求分发与响应封装。
- api 层 **禁止** 出现任何业务逻辑处理或抛出业务异常。
- 接口函数 **可以** 调用 Service 层的公有方法。
- 接口函数 **禁止** 直接调用任何 client 层方法方法。
- 接口函数 **禁止** 相互调用（一个 api 接口内部禁止调用另一个 api 接口）。
- Service 实例 **必须** 通过 `Depends` 注入，**禁止** 在 api 层手动实例化 Service 对象（如 `service = UserService()`）。
- 注入后的变量 **必须** 声明其具体类型（如 `service: UserService = Depends(get_user_service)`）。

## 注释形式规范

- 每个方法 **必须** 包含注释，注释内容 **必须** 明确说明该接口的业务功能及调用约束。
- 注释内容 **必须** 写在方法定义的正上方。
- 注释 **必须** 使用 `#` 符号。
- **禁止** 使用 `"""` 或 `'''`（文档字符串）进行注释。

## 日志记录规范

- api 文件 **必须** 使用 `__name__` 定义模块级 logger，且日志操作对象 **必须** 命名为 `_log`。
- 日志 **仅限** 用于记录接口调用信息和响应信息。
- **禁止** 在 api 层记录业务状态或业务处理结果。

## 实例创建规范

- 由于 api 层 **禁止** 定义类，而是使用路由定义 Api 接口，因此 **必须** 在模块内创建路由实例，**禁止** 创建任何其它实例。
- 路由对象变量名 **统一** 使用 `router`（如 `router = APIRouter()`）。
- 路由对象 `router` **必须** 在模块内完成实例化。
- api 文件 **必须** 仅作为路由挂载点，具体的路由聚合（Include Router）操作 **必须** 在应用启动获初始化入口（如 `main.py`，`application.py`）完成。

## 标准示例

```python
import logging
from fastapi import APIRouter, Depends

router = APIRouter()
_log = logging.getLogger(__name__)

# xxx 接口
@router.post("/v1/xxx", response_model=ApiResponse)
async def xxx(
    dto: XxxDTO,
    service: XxxService = Depends(get_xxx_service),
) -> ApiResponse:
    # 调用 xxx 业务服务
    result: XxxEntity = service.xxx(dto)
    # 映射响应体对象
    vo: XxxVO = ...
    # 返回统一响应
    return ApiResponse.success(vo)
```
