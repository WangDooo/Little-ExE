from PreProcess import *

# 边坡尺寸参数设定
H = 5
alpha_slope = 45
# 土质参数
c_effective = 2
phi_effective = 30
# 条分数目
N = 20

# def coordinate(H,alpha_slope,c_effective,phi_effective,N):
c = coordinate(H,alpha_slope,c_effective,phi_effective,N)
# circle_center(beta_1,beta_2,alpha_slope,A_x,A_y,B_x,B_y)
center = circle_center(45,0,c['alpha_slope'],c['A_x'],c['A_y'],c['B_x'],c['B_y'])
print(center)
# circle_radius(center,B_x,B_y):
R = circle_radius(center,c['B_x'],c['B_y'])
print(R)
# def side_top(x,A_x,A_y,B_x,B_y,alpha_slope):
print(side_top(15.45,c['A_x'],c['A_y'],c['B_x'],c['B_y'],c['alpha_slope']))

# def point_left(center,radius,A_y)
point_left = point_left(center,R,c['A_y'])
# def point_right(center,radius,B_y)
point_right = point_right(center,R,c['B_y'])
# def slice_x(point_left,point_right,N)
slice_x = slice_x(point_left,point_right,c['N'])
print(slice_x)