import pytz

# 모든 시간대 목록 얻기
all_timezones = pytz.all_timezones
print(all_timezones)

# 특정 시간대 객체 얻기
korea = pytz.timezone('Asia/Seoul')
print(korea)

# 현재 시간에 시간대 적용하기
from datetime import datetime

current_time = datetime.now(korea)
print(current_time)