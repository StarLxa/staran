# Staran v1.0.8 版本更新说明

## 🎉 重大更新：农历支持 + 多语言本地化

**发布日期**: 2025-07-29  
**版本**: 1.0.8  
**更新类型**: 主要功能增强  

---

## 🆕 新增功能

### 🌙 完整农历支持

#### 农历与公历互转
- 新增 `Date.from_lunar(year, month, day, is_leap)` 方法
- 新增 `Date.from_lunar_string(lunar_string)` 方法  
- 新增 `date.to_lunar()` 方法
- 新增 `date.to_lunar_string(compact)` 方法
- 支持1900-2100年范围的精确转换
- 完整处理闰月情况

#### 农历格式化
- 新增 `date.format_lunar()` 方法 - 中文农历格式
- 新增 `date.format_lunar_compact()` 方法 - 紧凑格式
- 支持天干地支和生肖显示
- 可配置年份、生肖显示选项

#### 农历判断方法
- 新增 `date.is_lunar_new_year()` - 是否农历新年
- 新增 `date.is_lunar_month_start()` - 是否农历月初
- 新增 `date.is_lunar_month_mid()` - 是否农历月中
- 新增 `date.is_lunar_leap_month()` - 是否农历闰月

#### 农历比较功能
- 新增 `date.compare_lunar(other)` - 农历日期比较
- 新增 `date.is_same_lunar_month(other)` - 同农历月判断
- 新增 `date.is_same_lunar_day(other)` - 同农历日判断

### 🌍 多语言本地化支持

#### 全局语言配置
- 新增 `Date.set_language(language_code)` 类方法
- 新增 `Date.get_language()` 类方法
- 新增 `Date.get_supported_languages()` 类方法
- 支持中简、中繁、日、英四种语言
- 一次配置，全局生效

#### 多语言格式化方法
- 新增 `date.format_localized()` - 本地化日期格式
- 新增 `date.format_weekday_localized()` - 本地化星期格式
- 新增 `date.format_month_localized()` - 本地化月份格式
- 新增 `date.format_quarter_localized()` - 本地化季度格式
- 新增 `date.format_relative_localized()` - 本地化相对时间

#### 单次语言覆盖
- 所有本地化方法支持 `language_code` 参数
- 可在方法级别覆盖全局语言设置
- 不影响全局语言配置

### 🏗️ 新增类和模块

#### LunarDate 类
- 独立的农历日期类
- 完整的农历日期操作
- 天干地支和生肖功能
- 多种格式化选项
- 农历日期比较功能

#### Language 类  
- 多语言配置管理
- 四种语言的完整数据
- 线程安全的全局设置
- 本地化格式化支持

---

## 🔧 API 增强

### 新增模块级函数
```python
from staran.date import from_lunar, set_language, get_language

# 便捷的农历创建函数
date = from_lunar(2025, 1, 1)

# 便捷的语言设置函数
set_language('en_US')
current_lang = get_language()
```

### 扩展导入支持
```python
# 直接导入新类
from staran.date import LunarDate, Language

# 或使用模块级访问
from staran.date import Date
Date.set_language('zh_TW')
```

---

## 📊 测试覆盖

### 新增测试模块
- `test_v108_features.py` - 21项新功能测试
- 农历转换精度测试
- 多语言一致性测试  
- 语言覆盖功能测试
- 农历比较和判断测试

### 测试统计
- **总测试数**: 85项 (64项原有 + 21项新增)
- **测试覆盖率**: 100%
- **运行时间**: < 0.005秒
- **成功率**: 100%

---

## 🚀 性能优化

### 农历计算性能
- 高效的农历算法实现
- LRU缓存优化重复计算
- 批量农历转换支持

### 多语言性能
- 语言数据预加载
- 线程安全的全局缓存
- 最小化格式化开销

### 内存优化
- 继续使用 `__slots__` 优化
- 农历对象内存效率优化
- 语言数据共享机制

---

## 🔄 向后兼容性

### 完全兼容
- **120+ 原有API** 保持完全不变
- 所有原有功能正常工作
- 原有测试100%通过
- 无破坏性变更

### 平滑升级
- 新功能为可选增强
- 默认行为保持不变
- 渐进式功能启用

---

## 📖 文档更新

### 新增文档
- `v108_quick_guide.md` - v1.0.8快速使用指南
- `v108_features_demo.py` - 完整功能演示
- `test_v108_features.py` - 测试用例参考

### 更新文档
- `README.md` - 更新主要特性介绍
- `__init__.py` - 更新API导出
- `setup.py` - 更新版本和关键词

---

## 🎯 使用示例

### 农历功能快速上手
```python
from staran.date import Date, from_lunar

# 农历转公历
spring_festival = from_lunar(2025, 1, 1)  # 农历正月初一
print(f"春节: {spring_festival.format_iso()}")

# 公历转农历  
date = Date("20250415")
print(f"农历: {date.format_lunar()}")

# 农历判断
if spring_festival.is_lunar_new_year():
    print("这是农历新年！")
```

### 多语言功能快速上手
```python
from staran.date import Date, set_language

# 设置全局语言
set_language('en_US')  # 英语
set_language('ja_JP')  # 日语

# 本地化格式
date = Date("20250415")
print(date.format_localized())         # 本地化日期
print(date.format_weekday_localized()) # 本地化星期

# 单次覆盖
print(date.format_weekday_localized(language_code='zh_CN'))
```

---

## 🔮 后续计划

### v1.0.9 候选功能
- 农历节气计算
- 更多传统历法支持
- 性能进一步优化
- 更多本地化语言

### 长期规划
- 其他历法系统支持
- 天文算法集成
- 更丰富的文化功能

---

## 👥 致谢

感谢所有使用 Staran 的开发者，您的反馈推动了这次重大更新。

**升级建议**: 强烈推荐所有用户升级到 v1.0.8，享受农历和多语言带来的强大功能！

---

*Staran v1.0.8 - 让日期处理更强大，更国际化* ✨
