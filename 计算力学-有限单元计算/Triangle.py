# coding: utf-8
# 计算力学编程作业
# 王博臣 171030
###################
import numpy as np
from PreProcess import *

# 常量
maximum = 10000000000000

# 材料特性 弹性模量E 泊松比v
E = 1000 
v = 0.25

# 单元弹性矩阵D
def get_matrix_D(E,v):
    a = E/(1-v**2)
    D = np.array([[1,v,0],[v,1,0],[0,0,(1.0-v)/2]]) * a
    return D

# 单元应变矩阵 是整体坐标的常数矩阵
def get_matrix_B(csys_e):
	b = [0.0,0.0,0.0]
	c = [0.0,0.0,0.0]
	for i in range(3):
		b[i] = csys_e[(i+1)%3][1]-csys_e[(i+2)%3][1] # b1=y2-y3
		c[i] = csys_e[(i+2)%3][0]-csys_e[(i+1)%3][0] # c1=x3-x2
	# 面积根据公式计算
	A = 0.5*(b[0]*c[1]-b[1]*c[0]) # 也可以 A = get_unit_A_33(num)
	# 形成B矩阵
	B = (1.0/(2*A))*np.array([[b[0],0.0,b[1],0.0,b[2],0.0],[0.0,c[0],0.0,c[1],0.0,c[2]],[c[0],b[0],c[1],b[1],c[2],b[2]]])
	return B

# 计算单元刚度矩阵
def get_K(num):
	# 初始化 K
	K = init_K_33(num)
	node = get_Node_33(num)
	csys = get_Global_csys_33(num)
	for e in node:
		# 利用node从csys中找到csyc_e 为对应的坐标
		csys_e = csys[e]
		# 初始化 Ke
		Ke = np.zeros((6,6))
		# 单元弹性矩阵D
		D = get_matrix_D(E,v)
		# 单元应变矩阵B
		B = get_matrix_B(csys_e)
		# 单元面积A
		A = get_unit_A_33(num)
		Ke = np.dot(np.dot(B.T,D),B)*A
		# 合成总刚矩阵
		a1 = e[0]
		a2 = e[1]
		a3 = e[2]
		# np.ix_ 将两个一维整数数组转换为一个用于选取方形区域的索引器
		K[np.ix_([2*a1,2*a1+1,2*a2,2*a2+1,2*a3,2*a3+1],[2*a1,2*a1+1,2*a2,2*a2+1,2*a3,2*a3+1])] += Ke

		# 边界条件 大数法处理
		border = np.array([1,2,3,4])-1 # 约束1,2节点的位移
		for i in border:
			K[i,i] = maximum
	return K

# 计算等效荷载 传入单元数
def get_F_Pq(num): # P=-5 and q=-1
	# 初始化 F
	F = init_F_33(num)
	# 计算节点数
	num_node = get_num_node_33(num)
	for i in range(4,num_node,2):
		F[2*i-1] = -1 # 均布 y向
	F[2*2-1] = -0.5 #均布荷载的-1 分到每个节点上是0.5
	F[2*num_node-1] = -5.5
	return F

def get_F_P(num): # P=-5
	# 初始化 F
	F = init_F_33(num)
	# 计算节点数
	num_node = get_num_node_33(num)
	F[2*num_node-1] = -5
	return F

def get_u(K,F):
	u = np.linalg.solve(K,F)
	return u
