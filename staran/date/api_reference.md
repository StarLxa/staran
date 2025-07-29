# `staran.date` API 参考

本文档为 `staran.date` 模块中可用的所有功能提供了详细的参考。

## `Date` 类

该模块的核心。它代表一个特定的日期，并提供了一套丰富的操作和格式化方法。

### 初始化

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
```

### 创建方法 (`from_*`)

-   `from_string(date_string: str) -> Date`: 从字符串创建 `Date` 对象。
-   `from_timestamp(timestamp: Union[int, float]) -> Date`: 从 Unix 时间戳创建 `Date` 对象。
-   `from_date_object(date_obj: datetime.date) -> Date`: 从 `datetime.date` 实例创建 `Date` 对象。
-   `today() -> Date`: 获取表示今天日期的 `Date` 对象的类方法。

### 转换方法 (`to_*`)

-   `to_tuple() -> Tuple[int, int, int]`: 返回 `(year, month, day)`。
-   `to_dict() -> Dict[str, int]`: 返回 `{'year': y, 'month': m, 'day': d}`。
-   `to_date_object() -> datetime.date`: 转换为标准的 `datetime.date` 对象。
-   `to_datetime_object() -> datetime.datetime`: 转换为标准的 `datetime.datetime` 对象（时间部分为 00:00:00）。
-   `to_timestamp() -> float`: 返回 Unix 时间戳。

### 格式化方法 (`format_*`)

`Date` 对象会记住输入字符串的格式，并默认使用该格式。

-   `format_default() -> str`: 根据其原始输入格式格式化日期。
-   `format_iso() -> str`: `YYYY-MM-DD` (例如, "2025-04-15")。
-   `format_chinese() -> str`: `YYYY年MM月DD日` (例如, "2025年04月15日")。
-   `format_compact() -> str`: `YYYYMMDD` (例如, "20250415")。
-   `format_slash() -> str`: `YYYY/MM/DD` (例如, "2025/04/15")。
-   `format_dot() -> str`: `YYYY.MM.DD` (例如, "2025.04.15")。
-   `format_year_month() -> str`: `YYYY-MM` (例如, "2025-04")。
-   `format_year_month_compact() -> str`: `YYYYMM` (例如, "202504")。
-   `format_custom(fmt: str) -> str`: 使用自定义的 `strftime` 格式字符串格式化日期。

### Getter 方法 (`get_*`)

-   `get_weekday() -> int`: 星期几 (周一=0, 周日=6)。
-   `get_isoweekday() -> int`: ISO 星期几 (周一=1, 周日=7)。
-   `get_month_start() -> Date`: 当前月份的第一天。
-   `get_month_end() -> Date`: 当前月份的最后一天。
-   `get_year_start() -> Date`: 当前年份的第一天。
-   `get_year_end() -> Date`: 当前年份的最后一天。
-   `get_days_in_month() -> int`: 当前月份的总天数。
-   `get_days_in_year() -> int`: 当前年份的总天数 (365 或 366)。

### 布尔检查方法 (`is_*`)

-   `is_weekend() -> bool`: 如果是周六或周日，则为 `True`。
-   `is_weekday() -> bool`: 如果是工作日，则为 `True`。
-   `is_leap_year() -> bool`: 如果是闰年，则为 `True`。
-   `is_month_start() -> bool`: 如果是月份的第一天，则为 `True`。
-   `is_month_end() -> bool`: 如果是月份的最后一天，则为 `True`。
-   `is_year_start() -> bool`: 如果是 1 月 1 日，则为 `True`。
-   `is_year_end() -> bool`: 如果是 12 月 31 日，则为 `True`。

### 日期算术 (`add_*` / `subtract_*`)

这些方法返回一个新的 `Date` 对象，并保留原始格式。

-   `add_days(days: int) -> Date`
-   `subtract_days(days: int) -> Date`
-   `add_months(months: int) -> Date`
-   `subtract_months(months: int) -> Date`
-   `add_years(years: int) -> Date`
-   `subtract_years(years: int) -> Date`

### 计算方法 (`calculate_*`)

-   `calculate_difference_days(other: Date) -> int`: 计算两个 `Date` 对象之间的天数。
-   `calculate_difference_months(other: Date) -> int`: 计算两个 `Date` 对象之间的大致月数。

### 比较

`Date` 对象可以使用标准运算符进行比较：`==`, `!=`, `<`, `<=`, `>`, `>=`。

```python
Date("20250101") < Date("20250102")  # True
```

## 异常类

该模块定义了自定义异常，以便清晰地处理错误。

-   `DateError`: 所有日期相关错误的基类。
-   `InvalidDateFormatError`: 当输入字符串格式不正确时引发。
-   `InvalidDateValueError`: 当日期值无效时（例如月份为 13）引发。

## `DateLogger` 类

一个用于 `Date` 类的内置日志记录器，用于调试和监控。

-   `set_log_level(level)`: 设置日志级别 (例如, "DEBUG", "INFO", "WARNING")。
