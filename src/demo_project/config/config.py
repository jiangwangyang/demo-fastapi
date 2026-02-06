import importlib
import os

# 显式声明模块的公共导出变量
DATABASE_URL: str = ""
DATABASE_USERNAME: str = ""
DATABASE_PASSWORD: str = ""

# 1. 读取环境变量，指定环境标识（默认开发环境 dev，防止未配置时报错）
ENV = os.getenv("ENVIRONMENT", "dev").strip().lower()
# 2. 动态导入对应环境的配置模块（匹配 config_dev.py/config_prod.py）
config_module = importlib.import_module(f"demo_project.config.config_{ENV}")
# 3. 将导入的配置模块属性「全部暴露」，外部直接导入 config 即可使用
locals().update(vars(config_module))
