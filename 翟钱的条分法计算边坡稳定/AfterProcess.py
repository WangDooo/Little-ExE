import matplotlib.pyplot as plt

def draw_slope(c):
	ax = plt.subplot(111) # 一般都在ax中设置,不再plot中设置
	# 绘制边坡外框
	plt.title('Bishop', size=14)

	x_slope = [ [0,0],
				[0,c['A_x']],
				[c['A_x'],c['B_x']],
				[c['B_x'],c['width_bottom']],
				[c['width_bottom'],c['width_bottom']],
				[c['width_bottom'],0]]
	y_slope = [ [0,c['height_left']],
				[c['height_left'],c['height_left']],
				[c['A_y'],c['B_y']],
				[c['height_right'],c['height_right']],
				[c['height_right'],0],
				[0,0]] 

	print([c['A_x'],c['A_y']],[c['B_x'],c['B_y']])
	for i in range(len(x_slope)):
		plt.plot(x_slope[i],y_slope[i], color='r')
		plt.scatter(x_slope[i],y_slope[i], color='b')

	plt.show()
