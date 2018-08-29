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

# 采用高斯积分点
ksai1 = -0.57735 
ksai2 = -ksai1
Gauss_point = [[ksai1,ksai1,1.0],[ksai2,ksai1,1.0],[ksai2,ksai2,1.0],[ksai1,ksai2,1.0]]

# 单元应变矩阵 
def get_matrix_B_44(csys_e,ksai,yita): # 整体坐标与局部坐标的关系 ksai-ξyita-η
    B = np.zeros((3,8)) # 初始化B
    dNdkdy = np.zeros((2,4)) # 形函数对局部坐标的求导矩阵 用于计算雅克比矩阵 dN/dkasi dN/dyita
    ksai0 = np.array([-1,1,1,-1]) # 原点在中心 根据编号 横坐标ksai -1 1 1 -1
    yita0 = np.array([-1,-1,1,1]) # 原点在中心 根据编号 纵坐标ksai -1 -1 1 1
    dNdkdy[0,:] = 0.25*ksai0*(1+yita0*yita) # 形成求导矩阵 dN/dξ 
    dNdkdy[1,:] = 0.25*yita0*(1+ksai0*ksai) # 形成求导矩阵 dN/dη
    J = np.dot(dNdkdy,csys_e) # 点积运算 得到雅克比矩阵
    J_inverse = np.linalg.inv(J) # 逆矩阵运算 
    J_det = np.linalg.det(J) # 雅克比矩阵行列式
    dNdxy = np.dot(J_inverse,dNdkdy) # 左乘雅克比逆矩阵 得到 dN/dx dN/dy
    for i in range(4):
        B[0,i*2] = dNdxy[0,i] # ksai偏导数
        B[1,i*2+1] = dNdxy[1,i] # yita偏导数
        B[2,i*2] = dNdxy[1,i]
        B[2,i*2+1] = dNdxy[0,i] # 交错填入
    return B, J_det

def get_K_44(num):
	# 初始化 K
	K = init_K_44(num)
	node = get_Node_44(num)
	csys = get_Global_csys_44(num)
	for e in node:
		# 利用node从csys中找到csyc_e 为对应的坐标
		csys_e = csys[e]
		# 初始化 Ke
		Ke = np.zeros((8,8))
		# 单元弹性矩阵D
		D = get_matrix_D(E,v)
		# 单元应变矩阵B 带入高斯积分点
		for i in Gauss_point:
			B, J_det = get_matrix_B_44(csys_e,i[0],i[1])
			Ke += np.dot(np.dot(B.T, D), B) * i[2] * J_det
		# 合成总刚矩阵
		a1 = e[0]
		a2 = e[1]
		a3 = e[2]
		a4 = e[3]
		# np.ix_ 将两个一维整数数组转换为一个用于选取方形区域的索引器
		K[np.ix_([2*a1,2*a1+1,2*a2,2*a2+1,2*a3,2*a3+1,2*a4,2*a4+1],[2*a1,2*a1+1,2*a2,2*a2+1,2*a3,2*a3+1,2*a4,2*a4+1])] += Ke

		# 边界条件 大数法处理
		border = np.array([1,2,3,4])-1 # 约束1,2节点的位移
		for i in border:
			K[i,i] = maximum
	return K

# 计算等效荷载 传入单元数
def get_F_Pq_44(num): # P=-5 and q=-1
	# 初始化 F
	F = init_F_44(num)
	# 计算节点数
	num_node = get_num_node_44(num)
	# 积分计算等效荷载
	y1 = lambda x: 0.5*(1+x)
	y2 = lambda x: 0.5*(1-x)
	R1,err = integrate.quad(y1,-1,1)
	R2,err = integrate.quad(y2,-1,1)
	for i in range(4,num_node,2):
		F[2*i-1] = -(R1+R2)*0.5 # R1+R2的一半
	F[2*2-1] = -R1*0.5 # R1的一半
	F[2*num_node-1] = -5-R2*0.5 # 加上P=-5
	return F

def get_F_P_44(num): # P=-5
	# 初始化 F
	F = init_F_44(num)
	# 计算节点数
	num_node = get_num_node_44(num)
	# 积分计算等效荷载
	F[2*num_node-1] = -5 # P=-5
	return F


