import math
import numpy as np 


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
# 圆心坐标 半径

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

print(side_top(17.5))
