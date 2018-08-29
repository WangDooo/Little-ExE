import urllib.request
import os
import re
import time
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox


global video_addrs, title, video_num, Anum

video_addrs = []


def url_open(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
	response = urllib.request.urlopen(url)
	html = response.read()

	return html


def find_html(html):
	
	a = html.find('<li><a href="')
	
	while a != -1:
		b = html.find('" target="_blank"', a, a+255)
		if b != -1:
			video_addrs.append(html[a+13:b])
		else:
			b = a + 13

		a = html.find('<li><a href="', b)

	return video_addrs



def main():
 	 
	root = Tk()
	root.title("ifeng视频下载---By WDoo")
	
	Label(root, text="生成链接TXT，程序与1.TXT放在同一文件夹").grid(row=0, column=0)

	Label(root, text="点击生成，就会立即生成").grid(row=3, column=0)
	
	def download_all():


		with open('2.txt', encoding='utf-8',errors='ignore') as f:
			html = f.read()
			find_html(html)

		with open('1.txt', 'w') as f1:
			for i in range(len(video_addrs)):
				video_addrs[i] = str(i) + '. ##' + video_addrs[i] + '###\n'
				f1.write(video_addrs[i])

		with open('1-原版.txt', 'w') as f2:
			for i in range(len(video_addrs)):
				video_addrs[i] = str(i) + '. ##' + video_addrs[i] + '###\n'
				f2.write(video_addrs[i])

	Button(root, text="生成", width=10,command=download_all).grid(row=4, column=0, sticky=W, padx=10, pady=5)

	Button(root, text="关闭", width=10, command=root.quit).grid(row=4, column=1, sticky=E, padx=10, pady=5)

	mainloop()

if __name__ == '__main__':
    main()



