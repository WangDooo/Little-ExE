import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


#直线方程函数
def f_1(x, A, B):
    return A*x + B
 
#二次曲线方程
def f_2(x, A, B, C):
    return A*x*x + B*x + C
 
#三次曲线方程
def f_3(x, A, B, C, D):
    return A*x*x*x + B*x*x + C*x + D

#双曲线方程
def f_4(x, A, B):
    return A/x + B


x = [0.05,0.1,0.5,1.0,5.0,10.0,50.0,100.0]
soil_1 = [0.9891,0.9785,0.9008,0.8195,0.4759,0.3123,0.0833,0.0434]
soil_2 = [0.9915,0.9832,0.9214,0.8542,0.5395,0.3694,0.1049,0.0553]
soil_3 = [0.9936,0.9872,0.9391,0.8852,0.6067,0.4354,0.1336,0.0716]
soil_4 = [0.9923,0.9847,0.9279,0.8655,0.5627,0.3915,0.1140,0.0604]


#绘制散点
plt.scatter(x[:], soil_1[:], 25, "red")

# 连接各点
plt.plot(x, soil_1, "black")


#直线拟合与绘制
A1, B1 = optimize.curve_fit(f_1, x, soil_1)[0]
x1 = np.arange(0, 100, 0.1)
y1 = A1*x1 + B1
plt.plot(x1, y1, "blue")
 
#二次曲线拟合与绘制
A2, B2, C2 = optimize.curve_fit(f_2, x, soil_1)[0]
x2 = np.arange(0, 100, 0.1)
y2 = A2*x2*x2 + B2*x2 + C2 
plt.plot(x2, y2, "green")
 
#三次曲线拟合与绘制
A3, B3, C3, D3= optimize.curve_fit(f_3, x, soil_1)[0]
x3 = np.arange(0, 100, 0.1)
y3 = A3*x3*x3*x3 + B3*x3*x3 + C3*x3 + D3 
plt.plot(x3, y3, "purple")

# 双曲线拟合与绘制
A4, B4 = optimize.curve_fit(f_4, x, soil_1)[0]
x4 = np.arange(0, 100, 0.1)
y4 = A4/x4 + B4
plt.plot(x4, y4, "yellow")
 
plt.title("test")
plt.xlabel('x')
plt.ylabel('y')
 
plt.show()
flag_1 = True
flag_2 = True
flag_3 = True
flag_4 = True
for i in range(len(x)):
	delta_x = (x[i] - x[i-1])
	if (soil_1[i]<0.5) and (flag_1 == True):
		ans_1 = x[i]-((0.5-soil_1[i])/(soil_1[i-1] - soil_1[i])*delta_x)
		print("soil_1：",ans_1)
		flag_1 = False
	if (soil_2[i]<0.5) and (flag_2 == True):
		ans_2 = x[i]-((0.5-soil_2[i])/(soil_2[i-1] - soil_2[i])*delta_x)
		print("soil_2：",ans_2)
		flag_2 = False
	if (soil_3[i]<0.5) and (flag_3 == True):
		ans_3 = x[i]-((0.5-soil_3[i])/(soil_3[i-1] - soil_3[i])*delta_x)
		print("soil_3：",ans_3)
		flag_3 = False
	if (soil_4[i]<0.5) and (flag_4 == True):
		ans_4 = x[i]-((0.5-soil_4[i])/(soil_4[i-1] - soil_4[i])*delta_x)
		print("soil_4：",ans_4)
		flag_4 = False
		
