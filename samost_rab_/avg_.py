import re

# Чтение файла stdout.log и извлечение временных меток
with open('stdout.log', 'r') as file:
    lines = file.readlines()

time_measurements = []
for line in lines:
    if "Enter measure_me" in line:
        start_time = re.search(r'\d{2}:\d{2}:\d{2}', line).group()
    elif "Leave measure_me" in line:
        end_time = re.search(r'\d{2}:\d{2}:\d{2}', line).group()
        time_measurements.append((start_time, end_time))

# Вычисление времени выполнения и среднего значения
total_time = 0
for start_time, end_time in time_measurements:
    total_time += (int(end_time[:2]) - int(start_time[:2])) * 3600 + (int(end_time[3:5]) - int(start_time[3:5])) * 60 + (int(end_time[6:]) - int(start_time[6:]))

average_time = total_time / len(time_measurements)
print(f"Среднее время выполнения функции measure_me: {average_time} секунд")