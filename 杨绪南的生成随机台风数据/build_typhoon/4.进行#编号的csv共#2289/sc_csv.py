import csv

input_file = 'file.csv'
output_file = 'output.csv'
i = 1
with open(input_file,'r',newline='') as csv_in_file: # 如果不指定newline='',则每写入一行将有一空行被写入。
	with open(output_file,'w',newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		for row_list in filereader:
			if row_list[0] == '66666':
				filewriter.writerow(['#'+str(i)])
				filewriter.writerow(row_list)
				i += 1
			else:
				filewriter.writerow(row_list)
			

