import matplotlib.pyplot as plt

from random_walk import RandomWalk


# 多次随机游走
while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # 将所有的点都绘制出来
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(192, 108), dpi=10)
    point_numbers = range(rw.num_points-2)
    ax.scatter(rw.x_values[1:rw.num_points-1], rw.y_values[1:rw.num_points-1], c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=150)
    ax.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=1000)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=1000)
    ax.set_aspect('equal')  # 两条轴的刻度相等
    ax.get_xaxis().set_visible(False)   # 将坐标轴设为不可见
    ax.get_yaxis().set_visible(False)
    plt.show()

    # 用户控制
    keep_running = input("Make Another Walk? ([y]/n)")
    if keep_running == 'n':
        break
