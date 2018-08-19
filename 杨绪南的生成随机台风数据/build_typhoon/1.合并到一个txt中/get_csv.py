import glob
import os

input_path = 'CMABSTdata'
output_file = 'output_csv.txt'
filewriter = open(output_file,'a') # w 是写入 a 是追加写入

for input_file in glob.glob(os.path.join(input_path,'*.txt')):
	with open(input_file,'r',newline='') as filereader:
		for i in filereader:
			filewriter.write(i.strip()+'\n') 
		
filewriter.close()
