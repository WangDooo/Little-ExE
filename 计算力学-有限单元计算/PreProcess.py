# coding: utf-8
# 计算力学编程作业
# 王博臣 171030
###################

import numpy as np

# 由单元数计算节点数
def get_num_node_33(num):
	num_node = (round((num/2))+1)*2 # 四舍五入round() 
	return num_node

def get_num_node_44(num):
	num_node = (num+1)*2 
	return num_node

def get_num_node_84(num):
	num_node = num*8-(num-1)*3
	return num_node

# 初始化总体刚度矩阵
def init_K_33(num):
	num_node = get_num_node_33(num)
	K = np.zeros((num_node*2,num_node*2))
	return K

def init_K_44(num):
	num_node = get_num_node_44(num)
	K = np.zeros((num_node*2,num_node*2))
	return K

def init_K_84(num):
	num_node = get_num_node_84(num)
	K = np.zeros((num_node*2,num_node*2))
	return K

# 初始化荷载列阵
def init_F_33(num):
	num_node = get_num_node_33(num)
	F = np.zeros(num_node*2)
	return F

def init_F_44(num):
	num_node = get_num_node_44(num)
	F = np.zeros(num_node*2)
	return F

def init_F_84(num):
	num_node = get_num_node_84(num)
	F = np.zeros(num_node*2)
	return F

# 单元面积_33
def get_unit_A_33(num):
	# 单元边长
	length = 8.0/(round(num/2))
	A = length*1/2
	return A

# 3节点三角形 节点编号
def get_Node_33(num): # num 为单元数
	# 节点总数
	num_node = get_num_node_33(num) 
	# 初始化矩阵
	a = np.array([[0,0,0]])
	# 添加各单元编号
	for i in range(1,num_node-2,2):
		b = np.array([[i,i+1,i+3]])
		a = np.vstack((a, b))
		c = np.array([[i+3,i+2,i]])
		a = np.vstack((a, c))
	a = np.delete(a,0,0)
	a = a - 1
	return a

# 3节点三角形 整体坐标
def get_Global_csys_33(num): 
	# 节点总数
	num_node = get_num_node_33(num) 
	# 初始化矩阵
	a = np.array([[0.0,0.0]])
	# 单元边长
	length = 8.0/(round(num/2))
	# 添加各点整体坐标
	j_len = 0
	for i in range(1,num_node,2):
		b = np.array([[j_len,0]]) # 纵坐标为0
		a = np.vstack((a, b))
		c = np.array([[j_len,1]]) # 纵坐标为1
		a = np.vstack((a, c))
		j_len = j_len + length
	a = np.delete(a,0,0)
	return a

# 4节点四边形 节点编号
def get_Node_44(num): # num 为单元数
	# 节点总数
	num_node = get_num_node_44(num) 
	# 初始化矩阵
	a = np.array([[0,0,0,0]])
	# 添加各单元编号
	for i in range(1,num_node-2,2):
		b = np.array([[i,i+2,i+3,i+1]])
		a = np.vstack((a, b))
	a = np.delete(a,0,0)
	a = a - 1
	return a

# 4节点四边形 整体坐标
def get_Global_csys_44(num): # 整体坐标
	# 节点总数
	num_node = get_num_node_44(num) 
	# 初始化矩阵
	a = np.array([[0.0,0.0]])
	# 单元边长
	length = 8.0/num
	# 添加各点整体坐标
	j_len = 0
	for i in range(1,num_node,2):
		b = np.array([[j_len,0]]) # 纵坐标为0
		a = np.vstack((a, b))
		c = np.array([[j_len,1]]) # 纵坐标为1
		a = np.vstack((a, c))
		j_len = j_len + length
	a = np.delete(a,0,0)
	return a

# 8节点四边形 节点编号
def get_Node_84(num): # num 为单元数
	# 节点总数
	num_node = get_num_node_84(num) 
	# 初始化矩阵
	a = np.array([[0,0,0,0,0,0,0,0]])
	# 添加各单元编号
	for i in range(1,num_node-5,5):
		b = np.array([[i,i+3,i+5,i+6,i+7,i+4,i+2,i+1]])
		a = np.vstack((a, b))
	a = np.delete(a,0,0)
	a = a - 1
	return a

# 8节点四边形 整体坐标
def get_Global_csys_84(num): # 整体坐标
	# 节点总数
	num_node = get_num_node_84(num) 
	# 初始化矩阵
	a = np.array([[0.0,0.0]])
	# 单元边长的一半
	length = 8.0/num/2
	# 添加各点整体坐标
	j_len = 0
	for i in range(1,num_node-6,5):
		b = np.array([[j_len,0]]) # 纵坐标为0
		a = np.vstack((a, b))
		b = np.array([[j_len,0.5]]) # 纵坐标为0.5
		a = np.vstack((a, b))
		b = np.array([[j_len,1]]) # 纵坐标为1
		a = np.vstack((a, b))
		b = np.array([[j_len+length,0]]) # 纵坐标为0
		a = np.vstack((a, b))
		b = np.array([[j_len+length,1]]) # 纵坐标为1
		a = np.vstack((a, b))
		j_len = j_len + length*2
	b = np.array([[8.0,0.0],[8.0,0.5],[8.0,1.0]]) # 最后一列没在循环中 固定值添加
	a = np.vstack((a, b))
	a = np.delete(a,0,0)
	return a
