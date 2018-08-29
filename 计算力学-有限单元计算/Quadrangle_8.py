# coding: utf-8
# 计算力学编程作业
# 王博臣 171030
###################

import numpy as np
from scipy import integrate
from Triangle import *

# 常量
maximum = 10000000000000

# 材料特性 弹性模量E 泊松比v
E = 1000 
v = 0.25

# 采用高斯积分
a = 0.77460
b = 0
c = 0.30864
d = 0.49383
e = 0.79012
Gauss_point = [[-a,-a,c],[a,-a,c],[a,a,c],[-a,a,c],[-a,b,d],[a,b,d],[b,a,d],[b,-a,d],[b,b,e]]


# 单元应变矩阵 
def get_matrix_B_84(csys_e,ksai,yita): # 整体坐标与局部坐标的关系 ksai-ξyita-η
    B = np.zeros((3,16)) # 初始化B
    # 各个节点对ksai-ξyita-求偏导
    dN1dksai = 0.25*(yita-1)*(-ksai-yita-1)+0.25*(yita-1)*(1-ksai)
    dN1dyita = 0.25*(ksai-1)*(-ksai-yita-1)+0.25*(ksai-1)*(1-yita)
    dN2dksai = 0.5*2*ksai*(yita-1)
    dN2dyita = 0.5*(ksai**2-1)
    dN3dksai = 0.25*(1-yita)*(ksai-yita-1)+0.25*(1+ksai)*(1-yita)
    dN3dyita = 0.25*(-1)*(1+ksai)*(ksai-yita-1)+0.25*(-1)*(1+ksai)*(1-yita)
    dN4dksai = 0.5*(1-yita**2)
    dN4dyita = 0.5*(-2)*yita*(1+ksai)
    dN5dksai = 0.25*(1+yita)*(ksai+yita-1)+0.25*(1+yita)*(1+ksai)
    dN5dyita = 0.25*(1+ksai)*(ksai+yita-1)+0.25*(1+ksai)*(1+yita)
    dN6dksai = 0.5*(-2)*ksai*(1+yita)
    dN6dyita = 0.5*(1-ksai**2)
    dN7dksai = 0.25*(-1)*(1+yita)*(-ksai+yita-1)+0.25*(-1)*(1-ksai)*(1+yita)
    dN7dyita = 0.25*(1-ksai)*(-ksai+yita-1)+0.25*(1-ksai)*(1+yita)
    dN8dksai = 0.5*(-1)*(1-yita**2)
    dN8dyita = 0.5*(-2)*yita*(1-ksai)
    # 形函数对局部坐标的求导矩阵 用于计算雅克比矩阵 dN/dkasi dN/dyitac 
    dNdkdy = np.array([[dN1dksai,dN2dksai,dN3dksai,dN4dksai,dN5dksai,dN6dksai,dN7dksai,dN8dksai],[dN1dyita,dN2dyita,dN3dyita,dN4dyita,dN5dyita,dN6dyita,dN7dyita,dN8dyita]])
    J = np.dot(dNdkdy,csys_e) # 点积运算 得到雅克比矩阵
    J_det = np.linalg.det(J) # 雅克比矩阵行列式
    J_inverse = np.linalg.inv(J) # 逆矩阵运算 
    dNdxy = np.dot(J_inverse,dNdkdy) # 左乘雅克比逆矩阵 得到 dN/dx dN/dy
    for i in range(8): # 形成B矩阵
        B[0,i*2] = dNdxy[0,i] # ksai偏导数
        B[1,i*2+1] = dNdxy[1,i] # yita偏导数
        B[2,i*2] = dNdxy[1,i]
        B[2,i*2+1] = dNdxy[0,i] # 交错填入
    return B, J_det      

def get_K_84(num):
	# 初始化 K
	K = init_K_84(num)
	node = get_Node_84(num)
	csys = get_Global_csys_84(num)
	for e in node:
		# 利用node从csys中找到csyc_e 为对应的坐标
		csys_e = csys[e]
		# 初始化 Ke
		Ke = np.zeros((16,16))
		# 单元弹性矩阵D
		D = get_matrix_D(E,v)
		# 单元应变矩阵B 带入高斯积分点
		for i in Gauss_point:
			B, J_det = get_matrix_B_84(csys_e,i[0],i[1])
			Ke += np.dot(np.dot(B.T, D), B) * i[2] * J_det
		# 合成总刚矩阵
		a1 = e[0]
		a2 = e[1]
		a3 = e[2]
		a4 = e[3]
		a5 = e[4]
		a6 = e[5]
		a7 = e[6]
		a8 = e[7]
		# np.ix_ 将两个一维整数数组转换为一个用于选取方形区域的索引器
		K[np.ix_( [2*a1,2*a1+1,2*a2,2*a2+1,2*a3,2*a3+1,2*a4,2*a4+1,2*a5,2*a5+1,2*a6,2*a6+1,2*a7,2*a7+1,2*a8,2*a8+1],[2*a1,2*a1+1,2*a2,2*a2+1,2*a3,2*a3+1,2*a4,2*a4+1,2*a5,2*a5+1,2*a6,2*a6+1,2*a7,2*a7+1,2*a8,2*a8+1])] += Ke
		# 边界条件 大数法处理
		border = np.array([1,2,5,6])-1 # 约束1,3节点的位移
		for i in border:
			K[i,i] = maximum
	return K

# 计算等效荷载 传入单元数
def get_F_Pq_84(num): # P=-5 and q=-1
	# 初始化 F
	F = init_F_84(num)
	# 计算节点数
	num_node = get_num_node_84(num)
	# 积分计算等效荷载
	y1 = lambda x: 0.25*(1-x)*2*(-x)
	y2 = lambda x: 0.5*(1-x**2)*2
	y3 = lambda x: 0.25*(1+x)*2*(x)
	R1,err = integrate.quad(y1,-1,1)
	R2,err = integrate.quad(y2,-1,1)
	R3,err = integrate.quad(y3,-1,1)
	for i in range(8,num_node,5):
		F[2*i-1] = -(R1+R3)*0.5 # R1+R3的一半
	for i in range(5,num_node,5):
		F[2*i-1] = -R2*0.5
	F[2*3-1] = -R1*0.5 # R1的一半
	F[2*num_node-1] = -5-R3*0.5 # 加上P=-5
	return F

def get_F_P_84(num): # P=-5
	# 初始化 F
	F = init_F_84(num)
	# 计算节点数
	num_node = get_num_node_84(num)
	# 积分计算等效荷载
	F[2*num_node-1] = -5 # P=-5
	return F


