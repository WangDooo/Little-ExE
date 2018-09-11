from PreProcess import *
import matplotlib.pyplot as plt

def draw_slope(num,u):
	num_up = round(num/2) + 1
	num_node = get_num_node_33(num)
	x = list(range(num_up))
	for i in range(num_up):
		x[i] = i * (8/(num_up-1))
	y1 = [0 for i in range(num_up)]
	y2 = [0.0] # 第一个点不动
	for i in range(7,num_node*2,4):
		y2.append(u[i])
	# 绘制变形图
	plt.title('Triangle_3 deformation graph', size=14)
	plt.plot(x, y1, color='b', linestyle='--', marker='o', label='before')
	plt.plot(x, y2, color='r', linestyle='-', marker='o',label='afters')
	# 横纵轴标签
	plt.xlabel('x(m)', size=14)
	plt.ylabel('u', size=14)
	# 线名称
	plt.legend(loc='lower left')
	# E μ说明
	plt.text(0.1, u[-1]/3, 'E = 1000, μ= 0.25', size=13)
	plt.show()
