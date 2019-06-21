input_file = 'DFO-Data'
output_file_block0 = 'output_data_block0.csv'
output_file_final = 'output_data_final.csv'

flag_block = 0

filewriter_block0 = open(output_file_block0,'w')
filewriter_final = open(output_file_final,'w')

# 读取DFO-Data数据 生成 output_data_block0.csv
with open(input_file,'r',newline='') as filereader:
	for line in filereader:
		if flag_block == 1:
			x = line.split(' ')[0]
			y = line.split(' ')[1]
			filewriter_block0.write(x+','+y+'\n')
			flag_block = 0
		if line[0:11] == 'block no: 0':
			flag_block = 1
filewriter_block0.write('0,0\n')
filewriter_block0.close()

# 读取output_data_block0.csv数据 生成 output_data_final.csv
flag_y = -1
sum_x = 0
sum_y = 0

filewriter_final.write('x累加值,y变号累加值\n')
with open(output_file_block0,'r',newline='') as filereader_block:
	for line in filereader_block:	
		sum_x += float(line.split(',')[0])
		sum_y += float(line.split(',')[1])
		if float(line.split(',')[1])*flag_y <= 0:
			temp_x = str(sum_x-float(line.split(',')[0]))
			temp_y = str(sum_y-float(line.split(',')[1]))
			filewriter_final.write(temp_x+','+temp_y+'\n')
			sum_y = float(line.split(',')[1])
			flag_y *= -1

filewriter_final.close()