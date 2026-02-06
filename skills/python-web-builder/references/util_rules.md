# util 代码编写规范

## 定位说明

- util 层是**通用工具层**，仅提供**无状态、可复用的工具函数**。
- util **不关心业务、不依赖业务、不感知业务含义**。

## 文件命名规范

- 文件名 **必须** 以 `_util.py` 结尾。
- 文件名需明确表达工具用途（如 `time_util.py`, `hash_util.py`）。
- **禁止** 使用模糊命名（如 `utils.py`, `common.py`, `helper.py`, `tool.py`）。

## 类命名与定义规范

- util 层 **禁止** 定义类。
- 所有功能 **必须** 以顶层函数（Function）的形式实现。
- **禁止** 在模块内定义全局可变变量。

## 变量命名与定义规范

- 所有变量 **必须** 声明类型。
- 变量命名 **必须** 符合 `语义 + 类型后缀` 格式（如 `timestamp_int: int`, `date_str: str`）。
- `dict` 类型变量 **仅限** 在函数内部使用，**禁止** 作为函数入参或返回值。

## 方法命名与定义规范

- 在 util 层级，方法即指独立函数。
- 方法命名 **必须** 使用 **动词 + 名词** 格式，体现“工具行为”（如 `format_datetime`）。
- 方法命名 **禁止** 出现业务语义词（如 `check_user`, `build_order`, `process_logic`）。
- 方法入参 **必须** 显式声明类型，**禁止** 使用 `dict` 作为入参，**禁止** 使用可变默认参数（如 `[]`, `{}`）。
- 方法返回值 **必须** 显式声明类型，返回值 **必须** 是基础类型（int/str/bool/float）或含义明确的 tuple，**禁止** 返回 `dict` 类型数据。
- 如果方法入参和返回值可以为 None，**必须** 显式声明类型为 `类型 | None`。
- 每个方法 **必须** 编写注释，说明工具用途及返回数据含义。方法注释 **必须** 使用 `#` 符号并写在方法定义正上方，**禁止** 使用 `"""` 或 `'''`。

## 业务逻辑规范

- util 层 **必须** 保持**无状态**，严禁依赖或修改全局变量、外部对象。
- util 层 **必须** 只包含纯计算、格式转换或通用校验逻辑。
- util 层 **严禁（禁止）** 出现任何数据库访问、网络请求或 IO 操作。
- util 层 **严禁（禁止）** 调用任何 client 层、service 层、api 层或 config 配置。
- util 层 **禁止** 出现工具类之间的互相依赖（即 `util` 不可调用其他 `util`）。
- util 层函数 **可以** 被项目中所有层级调用。

## 注释形式规范

- 每个方法 **必须** 包含注释，注释内容 **必须** 明确说明该工具函数的具体用途以及返回值的含义。
- 注释内容 **必须** 写在方法定义的正上方。
- 注释 **必须** 使用 `#` 符号。
- **禁止** 使用 `"""` 或 `'''`（文档字符串）进行注释。

## 日志记录规范

- util 文件 **必须** 使用 `__name__` 定义模块级 logger，且日志操作对象 **必须** 命名为 `_log`。
- 日志 **仅限** 用于记录极少数工具运行时的关键异常。
- **禁止** 在 util 层记录任何业务状态、业务处理结果或频繁打印调试信息。

## 实例创建规范

- 由于 util 层严禁定义类，因此 **禁止** 涉及任何实例创建逻辑。
- 外部 **必须** 直接导入并调用模块内的函数。

## 标准示例

```python
import time
import uuid
import logging

_log = logging.getLogger(__name__)

# 获取当前秒级时间戳
def get_current_timestamp() -> int:
    timestamp_int: int = int(time.time())
    return timestamp_int

# 将时间戳格式化为标准日期时间字符串
def format_timestamp(timestamp_int: int) -> str:
    time_struct = time.localtime(timestamp_int)
    time_str: str = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
    return time_str

# 生成唯一标识符字符串
def generate_uuid() -> str:
    uuid_str: str = str(uuid.uuid4())
    return uuid_str

# 解析字符串为整数，失败返回 None
def parse_int(value_str: str) -> int | None:
    try:
        return int(value_str)
    except ValueError:
        _log.error("Failed to parse int from %s", value_str)
        return None
