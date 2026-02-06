# config 代码编写规范

## 定位说明

- config 层是**配置定义层**，仅用于**配置变量定义**与**环境配置聚合**。
- config 层 **不包含业务逻辑**、**不定义类**、**不定义函数**。

## 文件与命名规范

- 仅允许在 `src/demo_project/config/` 目录下维护配置。
- 通用入口文件必须命名为 `config.py`。
- 环境配置文件必须命名为 `config_dev.py`、`config_prod.py`。
- 配置变量名使用全大写 + 下划线风格（如 `DATABASE_URL`）。

## 变量定义规范

- **只允许定义变量**，禁止定义类和函数。
- 变量必须显式声明类型（如 `DATABASE_URL: str = ""`）。
- 不允许出现 `dict` 类型变量。
- 变量值应为**纯配置值**（字符串、数字、布尔等），不得包含业务计算逻辑。

## 环境配置加载规范（config.py）

- `config.py` 是配置入口文件，负责读取环境标识（如 `ENVIRONMENT`）。
- `config.py` 必须动态导入环境配置模块（`config_dev.py` / `config_prod.py`）。
- `config.py` 必须将环境配置变量暴露给外部统一使用。
- 只允许使用标准库进行环境读取与模块导入（如 `os`、`importlib`）。
- 禁止在 `config.py` 中写入任何业务逻辑或资源访问。

## 环境配置文件规范（config_dev.py / config_prod.py）

- 仅定义配置变量，不做任何计算与导入。
- 变量名必须与 `config.py` 中声明的名称一致。
- 变量名拼写必须准确（例如 `DATABASE_URL`，禁止写成 `DATABASE_RUL`）。
- 禁止在环境配置文件中读取环境变量或访问外部资源。

## 访问规范

- 业务代码统一 `from demo_project.config import config` 读取配置。
- 禁止在业务代码中直接导入 `config_dev.py` 或 `config_prod.py`。

## 示例

```python
# config.py
import importlib
import os

DATABASE_URL: str = ""
DATABASE_USERNAME: str = ""
DATABASE_PASSWORD: str = ""

ENV = os.getenv("ENVIRONMENT", "dev").strip().lower()
config_module = importlib.import_module(f"demo_project.config.config_{ENV}")
locals().update(vars(config_module))
```
