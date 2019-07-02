import re

re_dict = {'Re_a':'3', 'Re_b':'5', 'Re_Test':'Wang'}

with open('Test-keywords.py', "r", encoding="utf-8") as f:
	# readlines以列表的形式将文件读出
	lines = f.readlines()
 
with open('replace_done.py', "w", encoding="utf-8") as f_w:
	for line in lines:
		re_line = line
		for v in re_dict:
			re_line = re.sub(v, re_dict[v], re_line)
		f_w.writelines(re_line)


