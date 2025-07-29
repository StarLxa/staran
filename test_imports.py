#!/usr/bin/env python3

import sys
import traceback

print("Testing imports step by step...")

try:
    print("1. Testing core module import...")
    from staran.date.core import Date, DateRange, DateError, LunarDate, Language
    print("   ✅ Core module import successful")
    print(f"   Date class: {Date}")
except Exception as e:
    print(f"   ❌ Core module import failed: {e}")
    traceback.print_exc()

try:
    print("2. Testing extensions module import...")
    from staran.date.extensions import (
        Timezone, TimezoneInfo, TIMEZONE_AVAILABLE,
        DateExpressionParser, ParseResult, EXPRESSIONS_AVAILABLE,
        SolarTerms, SolarTerm, SOLAR_TERMS_AVAILABLE
    )
    print("   ✅ Extensions module import successful")
except Exception as e:
    print(f"   ❌ Extensions module import failed: {e}")
    traceback.print_exc()

try:
    print("3. Testing integrations module import...")
    from staran.date.integrations import (
        DateVisualization, ChartData, TimeSeriesPoint, VISUALIZATION_AVAILABLE,
        StaranAPIServer, StaranAPIHandler, API_SERVER_AVAILABLE
    )
    print("   ✅ Integrations module import successful")
except Exception as e:
    print(f"   ❌ Integrations module import failed: {e}")
    traceback.print_exc()

print("✅ All individual imports completed")
