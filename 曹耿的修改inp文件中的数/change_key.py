import re
import glob
import os

input_path = 'inp'


old_1 = '0.5,'
new_1 = '0.7,'
old_2 = 'Set-1RF, 3, -5418.'
new_2 = 'Set-1RF, 3, -5515.'


for input_file in glob.glob(os.path.join(input_path,'*.inp')):
	output_name = input_file.split('\\')[-1]
	with open(input_file,'r',newline='',encoding="utf-8") as f:
		lines = f.readlines()
		with open(output_name, "w", encoding="utf-8") as f_w:
			for line in lines:
				re_line = line.strip()
				if (re_line == old_1):
					re_line = new_1
				if (re_line == old_2):
					re_line = new_2
				f_w.writelines(re_line+'\n')



