import matplotlib.pyplot as plt


# 显示plt可设置的样式
print(plt.style.available)

# 设置数据
input_values = range(1, 1001)
squares = [value ** 2 for value in input_values]
triples = [value ** 3 for value in input_values]

# 生成图片数据结构
fig, ax = plt.subplots()

# 设置坐标轴显示属性
ax.set_title("Square Numbers", fontsize=24)     # fontsize表明字体大小
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.axis([0, 1100, 0, 1_100_000])    #限定坐标轴范围
# ax.ticklabel_format(style='plain')    # 启用此语句则指定常规计数法而非科学计数法

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

# 生成连续的线图
ax.plot(input_values, triples, linewidth=3)     # linewidth表明线条粗细
# 生成散点图。    注意：一次只能生成plt的第一幅图
# s表明绘制时使用的点的尺寸，color表示颜色
# ax.scatter(input_values, squares, color='red', s=1)
# 但除了指定单一颜色，还可以使用颜色映射来达到渐变效果
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Reds, s=1)
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()  # 显示图片

