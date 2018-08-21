import glob
import os

input_path = 'data'
output_file = 'output_'+input_path+'.csv'
filewriter = open(output_file,'a') # w 是写入 a 是追加写入

force = [50,100,150,200,300,400,500,600,700,800]


for input_file in glob.glob(os.path.join(input_path,'*.txt')):
	with open(input_file,'r',newline='') as filereader:
		list_txt = []
		for i in filereader:
			list_txt.append(float(i))

		if len(list_txt) ==0 or list_txt[-1] < 0.0508:
			filewriter.write(input_file+',')
			filewriter.write('没有大于0.0508'+'\n')

		for i in range(len(list_txt)):
			if list_txt[i] > 0.0508:
				ans = (0.0508 - list_txt[i-1])/(list_txt[i]-list_txt[i-1])*(force[i]-force[i-1])+force[i-1]
				filewriter.write(input_file+',')
				filewriter.write(str(ans)+'\n')
				break
filewriter.close()
