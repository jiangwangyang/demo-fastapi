---
name: python-web-builder
description: 从0开始搭建 Python Web 项目的端到端流程指导：需求分析与文档、技术选型、详细设计、环境与项目初始化、按模块测试优先实现并遵循项目分层与测试规则。用户要新建 Python Web/后端/API 项目、需要完整搭建路径与规范落地时使用。
---

# Python Web 项目搭建（从0到可运行）

## 概览

本技能用于引导用户完成“需求 → 技术选型 → 详细设计 → 初始化 → 测试优先实现 → 全量验收”的完整搭建流程，并严格遵守
`references/` 中的规则与模板。

## 规则

- 必须使用中文回答用户、编写文档和编写注释
- 项目文件必须使用 UTF-8 编码
- 任何实现与文档输出必须符合 `references/project_rules.md`

## 必须遵循的流程

### 0）需求收集

- 询问目标、范围、用户、核心功能、数据源、非功能需求、约束、时间计划、部署目标与偏好技术栈。
- 查找并确认仓库内的规则文档（如 `AGENTS.md`、`rules.md`、测试规则文档），承诺严格遵守。
- 打开 `references/project_rules.md` 并确认目录、文件、命名与层级职责约束。

### 1）需求文档

- 与用户共创需求文档（中文，简洁、可验收）。
- 使用 `references/requirements-template.md` 作为模板。
- 需求文档必须写入现有目录（禁止随意新增目录，除非规则允许）。

### 2）详细设计

- 提出 1–2 套可行技术方案（框架、ORM/DB、配置管理、测试框架、依赖管理、运行方式）。
- 与用户完成详细设计：模块边界、数据模型、API 设计、测试计划、实现顺序。
- 使用 `references/design-template.md` 作为模板。
- 明确模块清单与文件命名，必须满足 `references/project_rules.md` 的命名规则与分层约束。
- 若需要示例结构或写法，参考 `references/*_example.md`。

### 3）初始化环境与项目

- 按选型完成环境初始化（venv/uv/poetry 等）。
- 初始化项目骨架和必要配置，确保能成功启动（至少包含健康检查）。
- 在初始化完成后进行最小化启动验证。
- 初始化 README 文档，使用 `references/readme-template.md`。

### 4）按模块测试优先实现（强制）

- 每个模块/文件必须按以下顺序执行：
    1) 先写该模块的测试；
    2) 实现模块代码使测试通过；
    3) 才能开始下一个模块。
- 严格遵守分层职责、依赖方向、命名规范与类型/注释规范。

### 5）最终验收

- 运行全量测试并确保通过。
- 输出运行与测试说明（最小可运行指令）。
- 总结已交付模块与后续建议。

## 工程规范摘要（不可违反）

- 目录与命名：严格按 `references/project_rules.md` 的结构与文件后缀；禁止随意新增/删除/重命名目录。
- 分层与依赖：api 仅做请求分发；service 只负责业务；client 只负责外部访问；util 纯函数无状态。
- 类型与变量：变量必须显式类型；禁止在 api/service/client/util/test 的入参或返回使用 `dict`。
- 类与方法：api/util/config 禁止定义类；每层方法/类命名遵守规则；DTO 继承 `BaseModel`，Entity/VO 用 `@dataclass`。
- 注释与日志：所有类/方法/属性必须使用 `#` 注释；统一 `_log` 模块日志规范。
- 测试流程：严格执行“模块级测试优先”，测试未通过不得进入下一模块。

## 资源

### references/

- `requirements-template.md`：需求文档模板
- `design-template.md`：详细设计模板
- `readme-template.md`：README 模板
- `project_rules.md`：项目结构规则文档
- `application_example.md`：application 示例代码
- `api_example.md`：api 示例代码
- `client_example.md`：client 示例代码
- `config_example.md`：config 示例代码
- `model_example.md`：model 示例代码
- `service_example.md`：service 示例代码
- `test_example.md`：test 示例代码
- `util_example.md`：util 示例代码
