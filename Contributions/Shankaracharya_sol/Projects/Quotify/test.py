# # import time
from datetime import datetime, timedelta
# current_time = datetime.now()
# print(current_time)
# unique_id =current_time.strftime("%S%f")
# print(unique_id)

current_time = datetime.now()
current_hours = current_time.strftime("%H")
current_minutes = current_time.strftime("%M")
current = current_hours * 60 + current_minutes
print(current_time)
print()
print(current_hours)
print()
print(current_minutes)