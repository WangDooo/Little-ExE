import math
import numpy as np 
from sympy import *

# 几何关系、各点坐标、参数值
def coordinate(H,alpha_slope,c_effective,phi_effective,N):
	# 根据H推算的土坡尺寸
	height_left = 3*H
	height_right = 2*H
	height_slope = abs(height_left-height_right)
	alpha_slope = 45
	width_top = 3*H
	width_bottom = 6*H+H/math.tan(alpha_slope/180*math.pi)
	# 根据H值计算出A、B点坐标
	A_x = width_top
	A_y = height_left
	B_x = A_x + height_slope/math.tan(alpha_slope/180*math.pi)
	B_y = height_right
	# 以字典的形式返回值
	return { 'height_left':height_left,
			 'height_right':height_right,
			 'height_slope':height_slope,
			 'alpha_slope':alpha_slope,
			 'width_top':width_top,
			 'width_bottom':width_bottom,
			 'A_x':A_x,'A_y':A_y,'B_x':B_x,'B_y':B_y,
			 'c_effective':c_effective,
			 'phi_effective':phi_effective,
			 'N':N}

# 根据beta_1、beta_2推算出圆心位置
def circle_center(beta_1,beta_2,alpha_slope,A_x,A_y,B_x,B_y):
	a1 = math.tan((180-beta_1-alpha_slope)/180*math.pi) # beta_1过B点直线的斜率
	a2 = math.tan((beta_2)/180*math.pi) # beta_2过A点直线的斜率
	v1 = np.array([[-a1,1],[-a2,1]])
	v2 = np.array([B_y-a1*B_x,A_y-a2*A_x]) 
	return np.linalg.solve(v1,v2)

# 根据圆心坐标 计算OB长度为参考半径
def circle_radius(center,B_x,B_y):
	return math.sqrt((B_x-center[0])**2+(B_y-center[1])**2)

# 上边界的分段函数表达式
def side_top(x,A_x,A_y,B_x,B_y,alpha_slope):
	if x <= A_x:
		y = A_y
	elif x > A_x and x <= B_x:
		y = math.tan((180-alpha_slope)/180*math.pi)*(x-A_x)+A_y
	elif x > B_x:
		y = B_y
	return y

# 圆弧与左侧坡上地面的交点 横坐标值
def point_left(center,radius,A_y): # center 是 [x,y]
	a = center[0] # 圆 (x-a)**2+(y-b)** = r**2
	b = center[1]
	r = radius
	y = A_y
	x = Symbol('x')
	return  min(solve((x-a)**2+(y-b)**2-r**2,x))

# 圆弧与右侧坡下地面的交点 横坐标值
def point_right(center,radius,B_y): # center 是 [x,y]
	a = center[0] # 圆 (x-a)**2+(y-b)** = r**2
	b = center[1]
	r = radius
	y = B_y
	x = Symbol('x')
	return  max(solve((x-a)**2+(y-b)**2-r**2,x))

# 分条的宽度
def slice_x(point_left,point_right,N):
	x = []
	width = abs(point_right-point_left)
	single_width = width / N
	temp = point_left
	for i in range(N+1):
		x.append(temp)
		temp += single_width
	return x

