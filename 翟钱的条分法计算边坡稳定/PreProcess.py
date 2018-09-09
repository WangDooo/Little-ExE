import math
import numpy as np 
from sympy import *

# 边坡尺寸参数设定
H = 5
height_left = 3*H
height_right = 2*H
height_slope = abs(height_left-height_right)
alpha_slope = 45
width_top = 3*H
width_bottom = 6*H+H/math.tan(alpha_slope/180*math.pi)
# 土质参数
c_effective = 2
phi_effective = 30
# 条分数目
N = 20

# 根据H值计算出A、B点坐标
x_A = width_top
y_A = height_left
x_B = x_A + height_slope/math.tan(alpha_slope/180*math.pi)
y_B = height_right

# 根据beta_1、beta_2推算出圆心位置
def circle_center(beta_1,beta_2):
	a1 = math.tan((180-beta_1-alpha_slope)/180*math.pi) # beta_1过B点直线的斜率
	a2 = math.tan((beta_2)/180*math.pi) # beta_2过A点直线的斜率
	v1 = np.array([[-a1,1],[-a2,1]])
	v2 = np.array([y_B-a1*x_B,y_A-a2*x_A]) 
	return np.linalg.solve(v1,v2)

# 根据圆心坐标 计算OB长度为参考半径
def circle_radius(center):
	return math.sqrt((x_B-center[0])**2+(y_B-center[1])**2)

# 上边界的分段函数表达式
def side_top(x):
	if x <= x_A:
		y = y_A
	elif x > x_A and x <= x_B:
		y = math.tan((180-alpha_slope)/180*math.pi)*(x-x_A)+y_A
	elif x > x_B:
		y = y_B
	return y

# 圆弧与左侧坡上地面的交点 横坐标值
def point_left(center,radius): # center 是 [x,y]
	a = center[0] # 圆 (x-a)**2+(y-b)** = r**2
	b = center[1]
	r = radius
	y = y_A
	x = Symbol('x')
	return  min(solve((x-a)**2+(y-b)**2-r**2,x))

# 圆弧与右侧坡下地面的交点 横坐标值
def point_right(center,radius): # center 是 [x,y]
	a = center[0] # 圆 (x-a)**2+(y-b)** = r**2
	b = center[1]
	r = radius
	y = y_B
	x = Symbol('x')
	return  max(solve((x-a)**2+(y-b)**2-r**2,x))

# 分条的宽度
def slice_top_bottom(point_left,point_right):
	top_bottom = []
	width = abs(point_right-point_left)
	single_width = width / N
	for i in range(N):
		temp_top =  \
	slice_top = side_top()
	pass

