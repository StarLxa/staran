#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Staran - 企业级日期处理库
========================

现代化Python日期处理库，专为企业应用设计。

主要特性：
- 🚀 统一的API命名约定 (from_*, to_*, get_*, is_*, add_*/subtract_*)
- 🧠 智能格式记忆 (保持输入格式类型)
- 📊 企业级日志记录 (可配置级别和输出)
- 🛡️ 强类型支持和完整错误处理
- 🧪 100%测试覆盖率 (64+综合测试)
- 📦 零外部依赖 (仅使用Python标准库)
- 🔄 向后兼容性 (支持旧API)

快速开始：
    >>> import staran
    >>> today = staran.today()
    >>> print(today)
    20250729
    
    >>> date = staran.from_string("20250415")
    >>> print(date.format_chinese())
    2025年04月15日
    
    >>> future = date.add_months(3)
    >>> print(future)
    20250715

更多示例：
    >>> from staran import Date
    >>> 
    >>> # 创建日期
    >>> d1 = Date(2025, 4, 15)
    >>> d2 = Date.from_string("202504")  # 智能解析
    >>> d3 = Date.today()
    >>> 
    >>> # 格式化输出
    >>> print(d1.format_iso())         # 2025-04-15
    >>> print(d1.format_chinese())     # 2025年04月15日
    >>> print(d1.format_compact())     # 20250415
    >>> 
    >>> # 日期运算 (保持格式)
    >>> print(d2.add_months(2))        # 202506
    >>> print(d1.subtract_days(10))    # 20250405
    >>> 
    >>> # 日期查询
    >>> print(d1.get_weekday())        # 1 (星期二)
    >>> print(d1.is_weekend())         # False
    >>> print(d1.get_month_end())      # 20250430

项目链接：https://github.com/your-username/staran
文档：https://staran.readthedocs.io/
"""

__version__ = "1.0.1"
__author__ = "Staran Team"
__email__ = "team@staran.dev"
__license__ = "MIT"

# 导入核心类和功能
from .core import Date, DateLogger

# 导出便捷函数
def today() -> Date:
    """
    创建今日的Date对象
    
    Returns:
        Date: 今日的Date对象
    
    Examples:
        >>> today = staran.today()
        >>> print(today)
        20250729
    """
    return Date.today()

def from_string(date_string: str) -> Date:
    """
    从字符串创建Date对象
    
    Args:
        date_string: 日期字符串 (支持YYYY, YYYYMM, YYYYMMDD格式)
    
    Returns:
        Date: 创建的Date对象
    
    Examples:
        >>> date = staran.from_string("20250415")
        >>> print(date.format_chinese())
        2025年04月15日
    """
    return Date.from_string(date_string)

# 定义公共API
__all__ = [
    'Date',
    'DateLogger', 
    'today',
    'from_string',
    '__version__',
    '__author__',
    '__email__',
    '__license__'
]
