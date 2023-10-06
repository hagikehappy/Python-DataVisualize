import requests
import plotly.express as px

# 执行API调用并查看响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 将响应转化为字典
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
# 处理结果
print(response_dict.keys())

# 探索有关仓库信息
repo_dicts = response_dict['items']     # 每个dict都包含一个仓库的所有信息
print(f"Repositories returned: {len(repo_dicts)}")
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # 添加可单击的URL
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 研究第一个仓库
# repo_dict = repo_dicts[0]   # 一个仓库字典中的每个项都是对仓库各方面属性的描述
# print(f"\nKeys:{len(repo_dict)}")
# for key in sorted(repo_dict.items()):
#     print(key)

# 可视化
title = "Most-Starred python Projects on Github"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
             hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)     # color指定为具有CSS名称的颜色，后者是不透明度
fig.show()




