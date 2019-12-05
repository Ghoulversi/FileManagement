from datetime import datetime

now = datetime.now()

current_time = now.strftime('%Hh%Mm%Ss')
print("Current time: " + current_time)