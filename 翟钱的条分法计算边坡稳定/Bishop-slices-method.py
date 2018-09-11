from PreProcess import *
from AfterProcess import *

# 边坡尺寸参数设定
H = 5
alpha_slope = 45
# 土质参数
c_effective = 2
phi_effective = 30
# 条分数目
N = 20

# c = coordinate(H,alpha_slope,c_effective,phi_effective,N)
# center = circle_center(45,0,c['alpha_slope'],c['A_x'],c['A_y'],c['B_x'],c['B_y'])
# R = circle_radius(center,c['B_x'],c['B_y'])
# point_left = point_left(center,R,c['A_y'])
# point_right = point_right(center,R,c['B_y'])
# slice_x = slice_x(point_left,point_right,c['N'])
# draw_slope(c,center,slice_x,R)