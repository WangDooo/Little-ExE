from tkinter import *
from tkinter import messagebox
import random
import time
import csv

total = 2290
need = 1000

def main():
 	 
	root = Tk()
	root.title("Typhoon Test")
	
	def show():
		num = 1
		li = [str(i) for i in range(1,total)]
		rli = random.sample(li, 1000)

		name_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()) 
		input_file = 'file.csv'
		output_file = 'M78星云传来的1000个数据'+name_time+'.csv'

		with open(input_file,'r',newline='') as csv_in_file: # 如果不指定newline='',则每写入一行将有一空行被写入。
			with open(output_file,'w',newline='') as csv_out_file:
				filereader = csv.reader(csv_in_file)
				filewriter = csv.writer(csv_out_file)
				for row_list in filereader:
					if row_list[0][1:] in rli:
						if row_list[1] == '66666':
							filewriter.writerow(['#'+str(num)])
							filewriter.writerow(row_list[1:]+['奥特曼'+str(num)+'号'])
							num += 1
						else:
							filewriter.writerow(['2018888888']+row_list[2:])

		
		messagebox.showinfo(title='可以毕业了！', message='搞定!来顿烧烤！')
		sys.exit()


	Button(root, text="杨哥！生成TM的1000个台风数据！",command=show).grid(row=0, column=0, sticky=W)

	mainloop()

if __name__ == '__main__':
    main()