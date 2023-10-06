from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
for index, column_header in enumerate(header_row):
    print(index, column_header)

# 提取最高温度
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(current_date)
    high = int(row[4])
    low = int(row[5])
    highs.append(high)
    lows.append(low)

# 根据最高温度绘图
plt.style.use('seaborn')    # 整体改变下一步中seaborn绘图的样式
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)   # alpha决定透明度
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)    # 将二者之间区域填充

# 设置绘图的格式
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()  # 将横坐标设置为倾斜式的，一般用于自动处理datetime格式数据
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.savefig('sitka_temperature.png', bbox_inches='tight')
plt.show()
