# second youngest  
# 1**6.1.27. it might be a birthday, beacuse we should buy flower for that day.
# isleap 闰年返回True
from calendar import isleap  
from datetime import date  
TUESDAY = 1  
for year in range(1006, 2000, 10):  
    t = date(year, 1, 27)  
    if isleap(year) and t.weekday() == TUESDAY:  
        print(t.isoformat())
