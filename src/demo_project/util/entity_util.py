# 实体类属性拷贝工具函数
# :param source_obj: 源实体对象（提供属性值）
# :param target_obj: 目标实体对象（接收属性值，直接修改原对象）
# :return: 无返回值，直接修改target_obj
def copy_entity_properties(source_obj, target_obj):
    # 1. 提取源对象的所有属性（键值对），__dict__是实体类属性的核心存储
    source_attrs = source_obj.__dict__

    # 2. 提取目标对象的所有有效属性名（过滤内置属性）
    target_valid_attrs = [attr for attr in dir(target_obj) if not attr.startswith('__')]

    # 3. 求属性交集：仅拷贝源和目标都存在的属性
    common_attrs = set(source_attrs.keys()) & set(target_valid_attrs)

    # 4. 循环拷贝属性值到目标对象
    for attr in common_attrs:
        setattr(target_obj, attr, source_attrs[attr])
