from pathlib import Path
import json
import plotly.express as px
import pandas as pd


# 将数据作为字符串读取并转化为Python对象，确认识别中文
path = Path('eq_data/eq_data_30_day_m1.geojson')
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)
# 将数据转化为更易读的格式
path = Path('eq_data/readable_eq_data.geojson')
if not path.exists():
    readable_contents = json.dumps(all_eq_data, indent=4)
    path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']  # 这里是一个由字典为元素构成的列表，其中每个字典都包含了一次地震的全部信息
# print(len(all_eq_dicts))

# 提取所有震级等关键信息
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
# print(mags[:10])
# print(titles[:10])
# print(lons[:10])
# print(lats[:10])

# 用pandas库中的方式封装数据
data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)
print(data.head()) # 相当于print前几行，默认是5

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    labels={'x': '经度', 'y': '纬度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    color='震级',  # 指定颜色根据震级大小而深浅
    hover_name='位置',    # 给指向散点的说明添加标题
)
fig.write_html('global_earthquakes.html')
fig.show()

