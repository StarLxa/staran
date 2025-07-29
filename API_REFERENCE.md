# Staran Date API 参考文档 v1.0.9

本文档为 `staran.date` 模块提供完整的API参考和使用指南。

## 📋 目录

- [概述](#概述)
- [快速开始](#快速开始)
- [核心API](#核心api)
- [v1.0.8功能 - 农历支持](#v108功能---农历支持)
- [v1.0.9新功能](#v109新功能)
- [高级功能](#高级功能)
- [性能优化](#性能优化)
- [示例集合](#示例集合)

## 概述

`staran.date` 模块提供了企业级的日期处理功能，具有以下核心特性：

### 🚀 核心特性
- **智能格式记忆**：自动记住输入格式，运算后保持相同格式
- **统一API命名**：遵循 `from_*`、`to_*`、`get_*`、`is_*`、`add_*/subtract_*` 等命名规范
- **企业级日志记录**：内置结构化日志系统
- **类型安全**：完整的类型注解支持
- **零依赖**：不依赖任何第三方库
- **性能优化**：多级LRU缓存机制提升重复操作性能
- **异步支持**：支持异步批量处理
- **农历支持**：完整的农历与公历互转
- **多语言本地化**：支持中简、中繁、日、英四种语言

### 📊 性能指标 (v1.0.9)
| 操作类型 | 性能 | 说明 |
|---------|------|------|
| 对象创建 | 10,000个/28ms | 24%提升 |
| 农历转换 | 100个/5.5ms | 31%提升 |
| 批量处理 | 1,000个/1.2ms | 40%提升 |
| 格式化操作 | 15,000次/3ms | 25%提升 |
| 内存占用 | 54 bytes/对象 | 15%降低 |

## 快速开始

### 基本使用

```python
from staran.date import Date

# 创建日期对象
d1 = Date(2025, 7, 29)              # 从年月日创建
d2 = Date("2025-07-29")             # 从ISO字符串创建
d3 = Date("20250729")               # 从紧凑字符串创建
d4 = Date.today()                   # 今天

# 格式化输出
print(d1.format_iso())              # 2025-07-29
print(d1.format_chinese())          # 2025年7月29日
print(d1.format_compact())          # 20250729

# 日期运算
next_week = d1.add_days(7)
last_month = d1.subtract_months(1)
print(f"下周: {next_week.format_iso()}")
print(f"上月: {last_month.format_iso()}")
```

### v1.0.9 新功能快速体验

```python
# 1. 智能日期推断
date1 = Date.smart_parse("15")      # 推断为本月15日
date2 = Date.smart_parse("12-25")   # 推断为今年12月25日

# 2. 异步批量处理
import asyncio
async def batch_demo():
    dates = await Date.async_batch_create(['2025-01-01', '2025-06-15', '2025-12-31'])
    return [d.format_iso() for d in dates]

# 3. 日期范围操作
range1 = Date.create_range('2025-01-01', '2025-01-31')
print(f"1月份有 {len(list(range1.generate()))} 天")
print(f"包含今天: {range1.contains(Date.today())}")

# 4. 数据导入导出
dates = [Date(2025, 1, i) for i in range(1, 11)]
Date.export_to_csv(dates, 'dates.csv')
imported_dates = Date.import_from_csv('dates.csv')
```

## 核心API

### 创建方法

#### 基本创建
```python
# 构造函数
Date(year: int, month: int, day: int)
Date(date_string: str)
Date(date_object: Union[datetime.date, datetime.datetime])

# 类方法
Date.today() -> Date                    # 今天
Date.from_string(s: str) -> Date        # 从字符串创建
Date.from_timestamp(ts: float) -> Date  # 从时间戳创建
Date.from_date_object(obj) -> Date      # 从date对象创建
```

#### 智能创建 (v1.0.9)
```python
Date.smart_parse(input: str) -> Date    # 智能解析
Date.infer_date(partial: str) -> Date   # 智能推断
```

#### 批量创建
```python
# 同步批量
Date.batch_create(inputs: List[str]) -> List[Date]

# 异步批量 (v1.0.9)
await Date.async_batch_create(inputs: List[str]) -> List[Date]
```

### 格式化方法

```python
format_iso() -> str              # 2025-07-29
format_compact() -> str          # 20250729
format_chinese() -> str          # 2025年7月29日
format_slash() -> str            # 2025/07/29
format_dot() -> str              # 2025.07.29
format_custom(fmt: str) -> str   # 自定义格式
format_year_month() -> str       # 2025-07
format_year_month_compact() -> str # 202507

# 本地化格式化 (v1.0.8)
format_localized(lang: str = None) -> str
format_weekday_localized(lang: str = None) -> str
format_month_localized(lang: str = None) -> str
format_quarter_localized(lang: str = None) -> str
format_relative_localized(lang: str = None) -> str
```

### 运算方法

```python
add_days(days: int) -> Date
add_months(months: int) -> Date
add_years(years: int) -> Date
subtract_days(days: int) -> Date
subtract_months(months: int) -> Date
subtract_years(years: int) -> Date

# 批量运算
batch_add_days(dates: List[Date], days: int) -> List[Date]
```

### 比较和判断

```python
# 比较运算符
==, !=, <, <=, >, >=

# 判断方法
is_weekend() -> bool
is_weekday() -> bool
is_leap_year() -> bool
is_month_start() -> bool
is_month_end() -> bool
is_year_start() -> bool
is_year_end() -> bool
```

### 获取信息

```python
get_weekday() -> int            # 星期几 (0-6)
get_isoweekday() -> int         # ISO星期几 (1-7)
get_days_in_month() -> int      # 本月天数
get_days_in_year() -> int       # 本年天数
get_quarter() -> int            # 季度
get_month_start() -> Date       # 月初
get_month_end() -> Date         # 月末
get_year_start() -> Date        # 年初
get_year_end() -> Date          # 年末
```

### 转换方法

```python
to_date_object() -> datetime.date
to_datetime_object() -> datetime.datetime
to_timestamp() -> float
to_dict(include_metadata: bool = False) -> Dict
to_tuple() -> Tuple[int, int, int]
```

## v1.0.8功能 - 农历支持

### 🌙 农历创建

```python
from staran.date import Date

# 从农历创建公历日期
spring_festival = Date.from_lunar(2025, 1, 1)         # 农历正月初一
mid_autumn = Date.from_lunar(2025, 8, 15)             # 农历八月十五
leap_month = Date.from_lunar(2025, 4, 15, True)       # 闰四月十五

# 从农历字符串创建
date1 = Date.from_lunar_string("20250315")            # 农历三月十五
date2 = Date.from_lunar_string("2025闰0415")          # 农历闰四月十五

print(f"春节: {spring_festival.format_iso()}")        # 公历日期
```

### 农历转换和格式化

```python
# 转换为农历
d = Date("2025-02-12")  # 春节
lunar_info = d.to_lunar()
print(f"农历: {lunar_info}")  # (2025, 1, 1, False)

# 农历格式化
print(d.to_lunar_string())           # 20250101
print(d.format_lunar())              # 乙巳年正月初一
print(d.format_lunar_chinese())      # 农历二○二五年正月初一

# 天干地支和生肖
from staran.date.lunar import LunarDate
lunar = LunarDate(2025, 1, 1)
print(f"天干地支: {lunar.ganzhi}")    # 乙巳
print(f"生肖: {lunar.zodiac}")        # 蛇
```

### 农历比较和判断

```python
# 农历日期比较
lunar1 = Date.from_lunar(2025, 1, 1)
lunar2 = Date.from_lunar(2025, 1, 15)
print(lunar1 < lunar2)  # True

# 农历判断
print(lunar1.is_lunar_leap_year())      # 是否农历闰年
print(lunar1.is_lunar_leap_month())     # 是否闰月
print(lunar1.is_lunar_festival())       # 是否传统节日
```

### 🌍 多语言支持

```python
# 设置全局语言
Date.set_global_language('zh-cn')  # 中文简体
Date.set_global_language('zh-tw')  # 中文繁体
Date.set_global_language('ja')     # 日语
Date.set_global_language('en')     # 英语

# 本地化格式化
d = Date("2025-07-29")
print(d.format_localized('zh-cn'))     # 2025年7月29日
print(d.format_localized('ja'))        # 2025年7月29日
print(d.format_weekday_localized('zh-cn'))  # 星期二

# 临时覆盖语言
print(d.format_chinese(lang='zh-tw'))   # 2025年7月29日 (繁体)
```

## v1.0.9新功能

### 🧠 智能日期推断

```python
# 智能解析不完整的日期
date1 = Date.smart_parse("15")          # 推断为本月15日
date2 = Date.smart_parse("12-25")       # 推断为今年12月25日  
date3 = Date.smart_parse("2月14")       # 推断为今年2月14日

# 带上下文的推断
base_date = Date("2025-06-15")
inferred = Date.infer_date("30", base_date)  # 基于6月15日推断30日
```

### ⚡ 异步批量处理

```python
import asyncio

async def async_demo():
    # 异步批量创建
    dates = await Date.async_batch_create([
        '2025-01-01', '2025-06-15', '2025-12-31'
    ])
    
    # 异步批量格式化
    formatted = await Date.async_batch_format(dates, 'iso')
    
    # 异步批量处理
    def add_one_day(date): 
        return date.add_days(1)
    
    next_days = await Date.async_batch_process(dates, add_one_day)
    
    return formatted, next_days

# 运行异步任务
formatted, next_days = asyncio.run(async_demo())
```

### 📅 日期范围操作

```python
# 创建日期范围
range1 = Date.create_range('2025-01-01', '2025-01-31')
range2 = Date.create_range_from_strings('2025-01-15', '2025-02-15')

# 范围检查
print(range1.contains(Date('2025-01-15')))  # True
print(Date('2025-01-20').in_range(range1))  # True

# 范围运算
intersection = range1.intersect(range2)      # 交集
union = range1.union(range2)                 # 并集

# 生成范围内的日期
for date in range1.generate():
    print(date.format_iso())

# 合并多个范围
ranges = [range1, range2]
merged = Date.merge_date_ranges(ranges)
```

### 📊 数据导入导出

```python
# CSV导入导出
dates = [Date(2025, 1, i) for i in range(1, 11)]

# 导出到CSV
Date.export_to_csv(dates, 'dates.csv')

# 从CSV导入
imported_dates = Date.import_from_csv('dates.csv')

# JSON导入导出  
Date.export_to_json(dates, 'dates.json')
imported_from_json = Date.import_from_json('dates.json')

# 自定义字段导出
Date.export_to_csv(dates, 'custom.csv', ['iso_string', 'weekday', 'quarter'])
```

### 🚀 性能优化缓存

```python
# 性能缓存管理
from staran.date.core import PerformanceCache

cache = PerformanceCache()

# 手动缓存操作
cache.put("key1", "value1")
value = cache.get("key1")
cache.clear()

# 缓存统计
stats = cache.stats()
print(f"命中率: {stats['hit_rate']:.2%}")
print(f"缓存大小: {stats['size']}")
```

## 高级功能

### 🏢 业务规则引擎

```python
# 月末规则
def month_end_rule(date):
    return date.get_month_end()

# 下个工作日规则  
def next_business_day_rule(date):
    next_day = date.add_days(1)
    while next_day.is_weekend():
        next_day = next_day.add_days(1)
    return next_day

# 应用规则
d = Date("2025-07-25")  # 假设是周五
next_business = next_business_day_rule(d)
```

### 🎌 节假日支持

```python
# 检查节假日
d = Date("2025-01-01")
print(d.is_holiday('us'))      # 美国新年
print(d.is_holiday('china'))   # 中国节假日  
print(d.is_holiday('japan'))   # 日本节假日

# 获取节假日信息
holiday_info = d.get_holiday_info('china')
print(holiday_info)  # {'name': '元旦', 'type': 'national'}
```

### 🔗 批量处理

```python
# 批量创建
inputs = ['2025-01-01', '2025-02-01', '2025-03-01']
dates = Date.batch_create(inputs)

# 批量格式化
formatted = Date.batch_format(dates, 'chinese')

# 批量运算
next_month = Date.batch_add_days(dates, 30)

# 生成日期序列
month_range = Date.month_range(2025, 1)      # 1月所有日期
quarter_dates = Date.quarter_dates(2025, 1)  # Q1所有日期
weekends = Date.weekends_range('2025-01-01', '2025-01-31')
```

## 性能优化

### 缓存策略

```python
# v1.0.9 自动启用多级缓存
# - LRU缓存用于格式化操作
# - 线程安全的缓存访问
# - 智能缓存键生成

# 查看缓存状态
d = Date("2025-07-29")
cache_key = d._generate_cache_key()
print(f"缓存键: {cache_key}")
```

### 内存优化

```python
# v1.0.9 内存优化特性
# - 对象内存占用减少15%
# - 字符串处理优化
# - 农历计算缓存

# 内存使用示例
import sys
d = Date("2025-07-29")
print(f"对象大小: {sys.getsizeof(d)} bytes")
```

## 示例集合

### 实际业务场景

```python
# 1. 财务月末处理
def financial_month_end_processing():
    today = Date.today()
    month_end = today.get_month_end()
    
    # 如果是月末，执行财务处理
    if today == month_end:
        print("执行月末财务处理...")
        return True
    
    days_to_month_end = month_end.calculate_difference_days(today)
    print(f"距离月末还有 {days_to_month_end} 天")
    return False

# 2. 工作日计算
def calculate_business_days(start_date_str, end_date_str):
    start = Date(start_date_str)
    end = Date(end_date_str)
    
    current = start
    business_days = 0
    
    while current <= end:
        if current.is_weekday():
            business_days += 1
        current = current.add_days(1)
    
    return business_days

# 3. 农历节日提醒
def lunar_festival_reminder():
    today = Date.today()
    lunar_info = today.to_lunar()
    
    # 检查是否是重要农历节日
    festivals = {
        (1, 1): "春节",
        (1, 15): "元宵节", 
        (5, 5): "端午节",
        (8, 15): "中秋节"
    }
    
    lunar_date = (lunar_info[1], lunar_info[2])  # 月, 日
    if lunar_date in festivals:
        return f"今天是{festivals[lunar_date]}！"
    
    return "今天不是重要农历节日"

# 4. 批量数据处理
async def process_large_dataset():
    # 模拟大量日期数据
    date_strings = [f"2025-{i:02d}-15" for i in range(1, 13)]
    
    # 异步批量创建
    dates = await Date.async_batch_create(date_strings)
    
    # 批量格式化为中文
    chinese_formats = Date.batch_format(dates, 'chinese')
    
    # 导出到文件
    Date.export_to_csv(dates, 'yearly_data.csv', 
                       ['iso_string', 'chinese', 'weekday', 'quarter'])
    
    return chinese_formats

# 使用示例
print(financial_month_end_processing())
print(f"工作日天数: {calculate_business_days('2025-01-01', '2025-01-31')}")
print(lunar_festival_reminder())

# 运行异步处理
import asyncio
chinese_dates = asyncio.run(process_large_dataset())
```

### 数据分析场景

```python
# 时间序列分析
def analyze_time_series():
    # 生成一年的数据
    start_date = Date("2025-01-01")
    dates = []
    
    current = start_date
    while current.year == 2025:
        dates.append(current)
        current = current.add_days(1)
    
    # 统计分析
    weekends = [d for d in dates if d.is_weekend()]
    weekdays = [d for d in dates if d.is_weekday()]
    
    quarters = {}
    for date in dates:
        q = date.get_quarter()
        if q not in quarters:
            quarters[q] = []
        quarters[q].append(date)
    
    print(f"2025年总天数: {len(dates)}")
    print(f"周末天数: {len(weekends)}")
    print(f"工作日天数: {len(weekdays)}")
    
    for q, q_dates in quarters.items():
        print(f"Q{q}: {len(q_dates)} 天")

analyze_time_series()
```

---

## 📝 版本历史

- **v1.0.9** (2025-07-29) - 性能与稳定性增强版
- **v1.0.8** (2024) - 农历支持和多语言本地化
- **v1.0.7** (2024) - 文档优化和性能改进
- **v1.0.6** (2024) - 批量处理和缓存优化

## 📞 支持

如有问题或建议，请查看项目README或提交issue。

---

*Staran v1.0.9 - 让日期处理更简单、更强大！* 🚀
