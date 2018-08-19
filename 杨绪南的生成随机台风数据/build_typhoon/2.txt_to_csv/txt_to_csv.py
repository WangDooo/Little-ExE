
input_file = 'file.txt'
output_file = 'output.txt'
filewriter = open(output_file,'w')
with open(input_file, 'r', newline='') as filereader:
	for s in filereader:
		s = s.replace(',,',',')
		filewriter.write(s.strip()+'\n')
