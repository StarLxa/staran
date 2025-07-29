# `staran.date` API 参考

本文档为 `staran.date` 模块中可用的所有功能提供了详细的参考。

## 概述

`staran.date` 模块提供了企业级的日期处理功能，具有以下核心特性：

- **智能格式记忆**：自动记住输入格式，运算后保持相同格式
- **统一API命名**：遵循 `from_*`、`to_*`、`get_*`、`is_*`、`add_*/subtract_*` 等命名规范
- **企业级日志记录**：内置结构化日志系统
- **类型安全**：完整的类型注解支持
- **零依赖**：不依赖任何第三方库
- **性能优化**：关键方法使用 LRU 缓存提升性能

## 快速导入

```python
# 基础导入
from staran.date import Date, DateLogger, today, from_string

# 异常类导入
from staran.date import DateError, InvalidDateFormatError, InvalidDateValueError

# 完整导入
import staran.date as sdate
```

## `Date` 类

该模块的核心。它代表一个特定的日期，并提供了一套丰富的操作和格式化方法。

### 初始化方式

您可以通过多种方式创建 `Date` 对象：

```python
from staran.date import Date
import datetime

# 1. 通过年、月、日
d1 = Date(2025, 4, 15)

# 2. 通过字符串 (YYYY, YYYYMM, 或 YYYYMMDD)
d2 = Date("20250415")
d3 = Date("2025-04-15") # 分隔符将被忽略
d4 = Date("202504")     # 代表月初
d5 = Date("2025")       # 代表年初

# 3. 通过 datetime 对象
dt_obj = datetime.date(2025, 4, 15)
d6 = Date(dt_obj)

# 4. 通过关键字参数
d7 = Date(year=2025, month=4, day=15)

# 5. 今日日期
d8 = Date.today()

# 6. 使用便捷函数
d9 = today()              # 等同于 Date.today()
d10 = from_string("2025") # 等同于 Date.from_string("2025")
```

### 智能格式记忆示例

```python
# 格式记忆演示
year_only = Date("2025")           # 年份格式
year_month = Date("202504")        # 年月格式
full_date = Date("20250415")       # 完整格式

# 运算后保持原格式
print(year_only.add_years(1))      # "2026"
print(year_month.add_months(2))    # "202506"
print(full_date.add_days(10))      # "20250425"
```

### 创建方法 (`from_*`)

所有创建方法都是类方法，可以直接通过 `Date` 类调用：

-   **`from_string(date_string: str) -> Date`**: 从字符串创建 `Date` 对象
    ```python
    Date.from_string("20250415")  # 完整日期
    Date.from_string("202504")    # 年月
    Date.from_string("2025")      # 年份
    ```

-   **`from_timestamp(timestamp: Union[int, float]) -> Date`**: 从 Unix 时间戳创建
    ```python
    Date.from_timestamp(1735689600)  # 2025-01-01
    Date.from_timestamp(time.time()) # 当前时间
    ```

-   **`from_date_object(date_obj: datetime.date) -> Date`**: 从标准库对象创建
    ```python
    import datetime
    dt = datetime.date(2025, 4, 15)
    Date.from_date_object(dt)
    ```

-   **`today() -> Date`**: 获取今日日期
    ```python
    today = Date.today()
    print(today)  # 当前日期
    ```

### 转换方法 (`to_*`)

将 `Date` 对象转换为其他格式：

-   **`to_tuple() -> Tuple[int, int, int]`**: 返回 `(year, month, day)`
    ```python
    date = Date(2025, 4, 15)
    print(date.to_tuple())  # (2025, 4, 15)
    ```

-   **`to_dict() -> Dict[str, int]`**: 返回字典格式
    ```python
    print(date.to_dict())  
    # {'year': 2025, 'month': 4, 'day': 15}
    ```

-   **`to_date_object() -> datetime.date`**: 转换为标准 `datetime.date`
    ```python
    std_date = date.to_date_object()
    print(type(std_date))  # <class 'datetime.date'>
    ```

-   **`to_datetime_object() -> datetime.datetime`**: 转换为 `datetime.datetime`
    ```python
    dt = date.to_datetime_object()
    print(dt)  # 2025-04-15 00:00:00
    ```

-   **`to_timestamp() -> float`**: 返回 Unix 时间戳
    ```python
    timestamp = date.to_timestamp()
    print(timestamp)  # 1744934400.0
    ```

### 格式化方法 (`format_*`)

`Date` 对象会记住输入字符串的格式，并默认使用该格式：

-   **`format_default() -> str`**: 根据原始输入格式格式化
    ```python
    Date("2025").format_default()      # "2025"
    Date("202504").format_default()    # "202504"
    Date("20250415").format_default()  # "20250415"
    ```

-   **`format_iso() -> str`**: ISO 格式 `YYYY-MM-DD`
    ```python
    date.format_iso()  # "2025-04-15"
    ```

-   **`format_chinese() -> str`**: 中文格式 `YYYY年MM月DD日`
    ```python
    date.format_chinese()  # "2025年04月15日"
    ```

-   **`format_compact() -> str`**: 紧凑格式 `YYYYMMDD`
    ```python
    date.format_compact()  # "20250415"
    ```

-   **`format_slash() -> str`**: 斜杠格式 `YYYY/MM/DD`
    ```python
    date.format_slash()  # "2025/04/15"
    ```

-   **`format_dot() -> str`**: 点分格式 `YYYY.MM.DD`
    ```python
    date.format_dot()  # "2025.04.15"
    ```

-   **`format_year_month() -> str`**: 年月格式 `YYYY-MM`
    ```python
    date.format_year_month()  # "2025-04"
    ```

-   **`format_year_month_compact() -> str`**: 年月紧凑格式 `YYYYMM`
    ```python
    date.format_year_month_compact()  # "202504"
    ```

-   **`format_custom(fmt: str) -> str`**: 自定义格式
    ```python
    date.format_custom("%Y年%m月%d日")  # "2025年04月15日"
    date.format_custom("%A, %B %d, %Y")  # "Tuesday, April 15, 2025"
    ```

### Getter 方法 (`get_*`)

获取日期的各种属性和相关日期：

-   **`get_weekday() -> int`**: 星期几 (周一=0, 周日=6)
    ```python
    date.get_weekday()  # 1 (星期二)
    ```

-   **`get_isoweekday() -> int`**: ISO 星期几 (周一=1, 周日=7)
    ```python
    date.get_isoweekday()  # 2 (星期二)
    ```

-   **`get_month_start() -> Date`**: 当前月份的第一天
    ```python
    date.get_month_start()  # Date("20250401")
    ```

-   **`get_month_end() -> Date`**: 当前月份的最后一天
    ```python
    date.get_month_end()  # Date("20250430")
    ```

-   **`get_year_start() -> Date`**: 当前年份的第一天
    ```python
    date.get_year_start()  # Date("20250101")
    ```

-   **`get_year_end() -> Date`**: 当前年份的最后一天
    ```python
    date.get_year_end()  # Date("20251231")
    ```

-   **`get_days_in_month() -> int`**: 当前月份的总天数
    ```python
    date.get_days_in_month()  # 30 (4月有30天)
    ```

-   **`get_days_in_year() -> int`**: 当前年份的总天数
    ```python
    date.get_days_in_year()  # 365 (2025年不是闰年)
    ```

### 布尔检查方法 (`is_*`)

各种日期条件判断：

-   **`is_weekend() -> bool`**: 是否为周末
    ```python
    date.is_weekend()  # False (星期二)
    ```

-   **`is_weekday() -> bool`**: 是否为工作日
    ```python
    date.is_weekday()  # True (星期二)
    ```

-   **`is_leap_year() -> bool`**: 是否为闰年
    ```python
    date.is_leap_year()  # False (2025年)
    ```

-   **`is_month_start() -> bool`**: 是否为月初
    ```python
    Date("20250401").is_month_start()  # True
    date.is_month_start()              # False
    ```

-   **`is_month_end() -> bool`**: 是否为月末
    ```python
    Date("20250430").is_month_end()  # True
    date.is_month_end()              # False
    ```

-   **`is_year_start() -> bool`**: 是否为年初 (1月1日)
    ```python
    Date("20250101").is_year_start()  # True
    date.is_year_start()              # False
    ```

-   **`is_year_end() -> bool`**: 是否为年末 (12月31日)
    ```python
    Date("20251231").is_year_end()  # True
    date.is_year_end()              # False
    ```

### 日期算术 (`add_*` / `subtract_*`)

这些方法返回一个新的 `Date` 对象，并保留原始格式：

-   **日期加减**：
    ```python
    base_date = Date("20250415")
    
    # 加减天数
    future = base_date.add_days(10)      # "20250425"
    past = base_date.subtract_days(5)    # "20250410"
    
    # 加减月数
    next_month = base_date.add_months(2)     # "20250615"
    prev_month = base_date.subtract_months(1) # "20250315"
    
    # 加减年数
    next_year = base_date.add_years(1)     # "20260415"
    prev_year = base_date.subtract_years(2) # "20230415"
    ```

-   **智能日期调整**：
    ```python
    # 月末日期加月数的智能调整
    month_end = Date("20250131")  # 1月31日
    next_month = month_end.add_months(1)  # "20250228" (2月没有31日)
    
    # 闰年处理
    leap_day = Date("20240229")  # 2024年2月29日
    next_year = leap_day.add_years(1)  # "20250228" (2025年不是闰年)
    ```

### 计算方法 (`calculate_*`)

计算日期之间的差异：

-   **`calculate_difference_days(other: Date) -> int`**: 计算天数差
    ```python
    date1 = Date("20250415")
    date2 = Date("20250425")
    diff = date1.calculate_difference_days(date2)  # 10
    ```

-   **`calculate_difference_months(other: Date) -> int`**: 计算月数差（近似）
    ```python
    date1 = Date("20250415")
    date2 = Date("20250615")
    diff = date1.calculate_difference_months(date2)  # 2
    ```

### 比较操作

`Date` 对象支持所有标准比较运算符：

```python
date1 = Date("20250415")
date2 = Date("20250416")
date3 = Date("20250415")

# 相等比较
print(date1 == date3)  # True
print(date1 != date2)  # True

# 大小比较
print(date1 < date2)   # True
print(date1 <= date3)  # True
print(date2 > date1)   # True
print(date2 >= date1)  # True

# 排序
dates = [Date("20250417"), Date("20250415"), Date("20250416")]
sorted_dates = sorted(dates)
print([str(d) for d in sorted_dates])  # ['20250415', '20250416', '20250417']
```

## 异常处理

该模块定义了自定义异常，以便清晰地处理错误：

### 异常类层次结构

```
DateError (继承自 ValueError)
├── InvalidDateFormatError
└── InvalidDateValueError
```

### 异常详解

-   **`DateError`**: 所有日期相关错误的基类
    ```python
    try:
        # 一些日期操作
        pass
    except DateError:
        # 捕获所有日期相关错误
        pass
    ```

-   **`InvalidDateFormatError`**: 当输入字符串格式不正确时引发
    ```python
    from staran.date import InvalidDateFormatError
    
    try:
        Date("invalid-date-format")
    except InvalidDateFormatError as e:
        print(f"格式错误: {e}")
    ```

-   **`InvalidDateValueError`**: 当日期值无效时引发
    ```python
    from staran.date import InvalidDateValueError
    
    try:
        Date(2025, 13, 1)  # 13月不存在
    except InvalidDateValueError as e:
        print(f"日期值错误: {e}")
    ```

### 常见异常场景

```python
# 格式错误示例
try:
    Date("abc123")         # 包含字母
    Date("2025-13-45")     # 无效的月日
    Date("20251301")       # 13月
except InvalidDateFormatError:
    print("输入格式不正确")

# 数值错误示例
try:
    Date(2025, 2, 30)      # 2月没有30日
    Date(2025, 0, 1)       # 0月不存在
    Date(2025, 12, 32)     # 12月没有32日
except InvalidDateValueError:
    print("日期数值无效")
```

## `DateLogger` 类

企业级日志记录器，为 `Date` 类提供结构化的日志记录功能。

### 初始化

```python
from staran.date import DateLogger

# 创建日志记录器
logger = DateLogger("my_app.date")

# 使用默认名称
logger = DateLogger()  # 默认名称: 'staran.Date'
```

### 日志方法

```python
# 各级别日志记录
logger.debug("调试信息", extra_data="value")
logger.info("一般信息", operation="create_date")
logger.warning("警告信息", date_value="invalid")
logger.error("错误信息", error_type="format_error")
```

### 设置日志级别

```python
import logging

# 方法1: 通过字符串
logger.set_level("DEBUG")
logger.set_level("INFO")
logger.set_level("WARNING")

# 方法2: 通过常量
logger.set_level(logging.DEBUG)
logger.set_level(logging.INFO)

# 类级别设置 (影响所有Date实例)
Date.set_log_level("DEBUG")
```

### 日志输出格式

默认日志格式：
```
2025-07-29 10:30:45,123 - staran.Date - INFO - 创建Date对象: 2025-04-15, 格式: full
```

## 便捷函数

模块提供了一些便捷的顶级函数：

### `today()`

```python
from staran.date import today

# 等同于 Date.today()
current_date = today()
print(current_date)  # 当前日期
```

### `from_string()`

```python
from staran.date import from_string

# 等同于 Date.from_string()
date = from_string("20250415")
print(date)  # "20250415"
```

## 性能优化

模块内置了多项性能优化：

### LRU 缓存

关键方法使用 `functools.lru_cache` 进行缓存：

```python
# _create_with_same_format 方法使用缓存
# 重复创建相同格式的日期对象时性能更佳
date1 = Date("20250415")
date2 = date1.add_days(1)  # 利用缓存，性能更好
```

### 输入验证优化

```python
# 严格的格式验证，快速失败
try:
    Date("invalid123")  # 立即检测到非数字字符
except InvalidDateFormatError:
    pass  # 快速异常处理
```

## 最佳实践

### 1. 异常处理

```python
from staran.date import Date, DateError

def safe_create_date(date_input):
    try:
        return Date(date_input)
    except DateError as e:
        print(f"日期创建失败: {e}")
        return None
```

### 2. 格式保持

```python
# 利用格式记忆功能
def process_date_batch(date_strings):
    dates = []
    for date_str in date_strings:
        date = Date(date_str)
        # 运算后自动保持原格式
        future_date = date.add_months(3)
        dates.append(future_date)
    return dates
```

### 3. 类型注解

```python
from typing import List
from staran.date import Date

def calculate_business_days(start: Date, end: Date) -> List[Date]:
    business_days = []
    current = start
    while current <= end:
        if current.is_weekday():
            business_days.append(current)
        current = current.add_days(1)
    return business_days
```

### 4. 日志配置

```python
# 在应用初始化时配置日志
import logging
from staran.date import Date

# 配置应用日志
logging.basicConfig(level=logging.INFO)

# 设置Date模块日志级别
Date.set_log_level("WARNING")  # 只记录警告和错误
```

## 向后兼容

模块保持向后兼容的旧API：

```python
date = Date("20250415")

# 新API (推荐)
date.format_custom("%Y-%m-%d")
date.to_date_object()
date.get_weekday()

# 旧API (兼容性)
date.format("%Y-%m-%d")        # 等同于 format_custom
date.to_date()                 # 等同于 to_date_object
date.weekday()                 # 等同于 get_weekday
```

## 模块信息

```python
import staran

# 版本信息
print(staran.__version__)      # "1.0.4"
print(staran.__author__)       # "Staran Team"
print(staran.__license__)      # "MIT"
```
