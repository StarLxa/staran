# Staran v1.0.8 快速使用指南

## 🌙 农历功能

### 基本农历操作

```python
from staran.date import Date, from_lunar

# 1. 从农历创建公历日期
spring_festival = Date.from_lunar(2025, 1, 1)     # 农历正月初一
mid_autumn = Date.from_lunar(2025, 8, 15)         # 农历八月十五
leap_month = Date.from_lunar(2025, 4, 15, True)   # 闰四月十五（如果存在）

print(f"春节: {spring_festival.format_iso()}")
print(f"中秋: {mid_autumn.format_iso()}")

# 2. 从农历字符串创建
date1 = Date.from_lunar_string("20250315")        # 农历三月十五
date2 = Date.from_lunar_string("2025闰0415")      # 农历闰四月十五

# 3. 公历转农历
solar_date = Date("20250415")
lunar_date = solar_date.to_lunar()
print(f"公历 {solar_date.format_iso()} → 农历 {lunar_date.format_chinese()}")
```

### 农历格式化

```python
date = Date("20250415")

# 基本农历格式
print(date.format_lunar())                         # 农历2025年五月廿七
print(date.format_lunar(include_year=False))       # 五月廿七
print(date.format_lunar(include_zodiac=True))      # 乙巳(蛇)年五月廿七

# 紧凑格式
print(date.format_lunar_compact())                 # 20250527
print(date.to_lunar_string())                      # 20250527
print(date.to_lunar_string(compact=False))         # 农历2025年五月廿七
```

### 农历判断

```python
# 农历节日判断
spring_festival = Date.from_lunar(2025, 1, 1)
lantern_festival = Date.from_lunar(2025, 1, 15)

print(spring_festival.is_lunar_new_year())         # True
print(spring_festival.is_lunar_month_start())      # True
print(lantern_festival.is_lunar_month_mid())       # True

# 农历闰月判断
date = Date("20250415")
print(date.is_lunar_leap_month())                  # 是否在闰月
```

### 农历比较

```python
date1 = Date.from_lunar(2025, 1, 1)
date2 = Date.from_lunar(2025, 1, 15)
date3 = Date.from_lunar(2025, 2, 1)

# 农历日期比较
print(date1.compare_lunar(date2))                  # -1 (date1 < date2)
print(date2.compare_lunar(date1))                  # 1  (date2 > date1)

# 农历月份判断
print(date1.is_same_lunar_month(date2))            # True (同一农历月)
print(date1.is_same_lunar_month(date3))            # False (不同农历月)

# 农历日期判断
print(date1.is_same_lunar_day(date2))              # False (不同农历日)
```

## 🌍 多语言功能

### 全局语言设置

```python
from staran.date import Date, set_language, get_language

# 设置全局语言（一次设置，全局生效）
set_language('zh_CN')    # 中文简体
set_language('zh_TW')    # 中文繁体
set_language('ja_JP')    # 日语
set_language('en_US')    # 英语

# 查看当前语言
print(get_language())    # 当前设置的语言代码

# 查看支持的语言
print(Date.get_supported_languages())
```

### 多语言格式化

```python
date = Date("20250415")  # 2025年4月15日，星期二

# 设置为不同语言查看效果
for lang in ['zh_CN', 'zh_TW', 'ja_JP', 'en_US']:
    set_language(lang)
    print(f"{lang}: {date.format_localized()}")
    
# 输出:
# zh_CN: 2025年04月15日
# zh_TW: 2025年04月15日  
# ja_JP: 2025年04月15日
# en_US: 04/15/2025
```

### 星期和月份本地化

```python
set_language('zh_CN')
date = Date("20250415")

# 星期格式化
print(date.format_weekday_localized())             # 星期二
print(date.format_weekday_localized(short=True))   # 周二

# 月份格式化
print(date.format_month_localized())               # 四月
print(date.format_month_localized(short=True))     # 4月

# 季度格式化
print(date.format_quarter_localized())             # 第二季度
print(date.format_quarter_localized(short=True))   # Q2
```

### 相对时间本地化

```python
today = Date.today()
tomorrow = today.add_days(1)
yesterday = today.add_days(-1)
next_week = today.add_days(7)

set_language('zh_CN')
print(f"今天: {today.format_relative_localized()}")
print(f"明天: {tomorrow.format_relative_localized()}")
print(f"昨天: {yesterday.format_relative_localized()}")
print(f"下周: {next_week.format_relative_localized()}")

set_language('en_US')
print(f"Today: {today.format_relative_localized()}")
print(f"Tomorrow: {tomorrow.format_relative_localized()}")
print(f"Yesterday: {yesterday.format_relative_localized()}")
print(f"Next week: {next_week.format_relative_localized()}")
```

### 单次语言覆盖

```python
# 设置全局语言为中文
set_language('zh_CN')
date = Date("20250415")

# 正常使用全局语言
print(date.format_weekday_localized())                      # 星期二

# 单次覆盖为英语（不影响全局设置）
print(date.format_weekday_localized(language_code='en_US')) # Tuesday

# 仍然是全局中文设置
print(date.format_weekday_localized())                      # 星期二
print(get_language())                                       # zh_CN
```

## 🔄 农历 + 多语言组合

```python
# 中国传统节日多语言展示
festivals = [
    (Date.from_lunar(2025, 1, 1), "春节"),
    (Date.from_lunar(2025, 1, 15), "元宵节"),
    (Date.from_lunar(2025, 5, 5), "端午节"),
    (Date.from_lunar(2025, 8, 15), "中秋节"),
]

languages = ['zh_CN', 'zh_TW', 'ja_JP', 'en_US']

for date, festival in festivals:
    print(f"\n{festival} ({date.format_iso()})")
    for lang in languages:
        set_language(lang)
        print(f"  {lang}: {date.format_localized()} ({date.format_weekday_localized()})")
        print(f"        农历: {date.format_lunar()}")
```

## 🚀 实用示例

### 生日提醒系统

```python
def birthday_reminder(lunar_birthday_year, lunar_birthday_month, lunar_birthday_day):
    """农历生日提醒"""
    from datetime import datetime
    
    # 获取今年的农历生日公历日期
    current_year = datetime.now().year
    birthday_this_year = Date.from_lunar(current_year, lunar_birthday_month, lunar_birthday_day)
    
    today = Date.today()
    days_until_birthday = today.calculate_difference_days(birthday_this_year)
    
    if days_until_birthday == 0:
        return "今天是您的农历生日！"
    elif days_until_birthday > 0:
        return f"距离您的农历生日还有 {days_until_birthday} 天"
    else:
        # 已经过了，计算明年的
        next_year_birthday = Date.from_lunar(current_year + 1, lunar_birthday_month, lunar_birthday_day)
        days_until_next = today.calculate_difference_days(next_year_birthday)
        return f"距离您的农历生日还有 {days_until_next} 天"

# 使用示例
print(birthday_reminder(1990, 3, 15))  # 农历三月十五生日
```

### 多语言日历生成

```python
def generate_calendar_month(year, month, language='zh_CN'):
    """生成多语言月历"""
    set_language(language)
    
    # 月份第一天和最后一天
    first_day = Date(year, month, 1)
    last_day = first_day.get_month_end()
    
    print(f"\n=== {first_day.format_month_localized()} {year} ===")
    
    # 星期标题
    weekdays = []
    for i in range(7):
        temp_date = Date(2025, 7, 28 + i)  # 2025-07-28是星期一
        weekdays.append(temp_date.format_weekday_localized(short=True))
    print(" ".join(f"{day:>4}" for day in weekdays))
    
    # 月历内容
    current = first_day
    week_line = [""] * 7
    
    # 填充第一周的空白
    start_weekday = first_day.get_weekday()
    for i in range(start_weekday):
        week_line[i] = "    "
    
    while current <= last_day:
        weekday = current.get_weekday()
        week_line[weekday] = f"{current.day:>4}"
        
        if weekday == 6:  # 星期日，打印这一行
            print("".join(week_line))
            week_line = ["    "] * 7
        
        current = current.add_days(1)
    
    # 打印最后一行（如果不完整）
    if any(day != "    " for day in week_line):
        print("".join(week_line))

# 生成不同语言的日历
generate_calendar_month(2025, 4, 'zh_CN')
generate_calendar_month(2025, 4, 'en_US')
```

### 传统节气计算

```python
def find_solar_terms_2025():
    """查找2025年二十四节气对应的公历日期"""
    # 简化版本，实际节气计算更复杂
    
    solar_terms = [
        "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
        "立夏", "小满", "芒种", "夏至", "小暑", "大暑",
        "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
        "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"
    ]
    
    # 这里只是示例，实际需要天文计算
    set_language('zh_CN')
    
    print("2025年二十四节气（示例）:")
    for i, term in enumerate(solar_terms):
        # 简化计算，实际应使用天文算法
        approx_date = Date(2025, (i // 2) + 1, 5 + (i % 2) * 15)
        print(f"{term}: {approx_date.format_localized()} ({approx_date.format_weekday_localized()})")

find_solar_terms_2025()
```

## 📚 更多功能

查看完整的API文档和更多示例：

- [完整API参考](staran/date/api_reference.md)
- [基础使用示例](staran/date/examples/basic_usage.py)
- [增强功能示例](staran/date/examples/enhanced_features.py)
- [v1.0.8新功能演示](staran/date/examples/v108_features_demo.py)

## 🎯 最佳实践

1. **全局语言设置**: 在应用启动时设置一次全局语言，避免频繁切换
2. **农历缓存**: 对于大量农历转换，考虑缓存结果
3. **类型安全**: 使用类型注解提高代码质量
4. **错误处理**: 农历转换时注意处理边界情况和无效日期
5. **性能优化**: 批量操作时使用专门的批量API方法
