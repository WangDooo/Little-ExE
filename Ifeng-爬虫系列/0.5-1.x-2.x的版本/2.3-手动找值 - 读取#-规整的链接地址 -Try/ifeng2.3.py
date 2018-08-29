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
	
	a = html.find('##')
	
	while a != -1:
		b = html.find('***', a, a+255)
		if b != -1:
			video_addrs.append(html[a+2:b])
		else:
			b = a + 2

		a = html.find('##', b)

	return video_addrs

def find_pic(html):
	
	a = html.find('"videoLargePoster": "')
	b = html.find('",', a, a+255)
	pic = html[a+21:b]

	return pic

def find_video(html):
	
	a = html.find('"gqSrc":')
	b = html.find('\",', a, a+255)
	video = html[a+10:b]

	return video

def find_title(html):
	
	
	a = html.find('"name": "')
	b = html.find('",', a, a+60)
	title = html[a+9:b]


	title = title.replace(chr(34),'“')
	title = title.replace('|','')
	title = title.replace(chr(58),'：')
	title = title.replace('\\','')
	title = title.replace(chr(47),'')
	title = title.replace(chr(92),'')
	title = title.replace(chr(60),'')
	title = title.replace(chr(62),'')
	title = title.replace(chr(63),'？')
	title = title.replace('*','')
		
	return title

def download_tt(title, pic, video):

	pic_name = title + '.png'
	video_name = title + '.mp4'

	with open(pic_name, 'wb') as f1:
		pic_t = url_open(pic)
		f1.write(pic_t)

	with open(video_name, 'wb') as f2:
		video_t = url_open(video)
		f2.write(video_t)




def main():
 	 
	root = Tk()
	root.title("ifeng视频下载---By WDoo")
	
	Label(root, text=" 将1.txt放到要下载到的文件夹").grid(row=0, column=0)

	Label(root, text="选择下载到的目录").grid(row=3, column=0)
	
	def download_all():

		fname = askdirectory(title=u"选择保存到文件夹") 
		os.chdir(str(fname))



		with open('1.txt', encoding='utf-8',errors='ignore') as f:
			html = f.read()
			find_html(html)
		
		Anum = len(video_addrs)

		print('开始下载视频\n')

		for i in range(Anum):
			url_api = video_addrs[i]
			html = url_open(url_api).decode('UTF-8')

			title_k = find_title(html)
			pic_k = find_pic(html)
			video_k = find_video(html)
			
			try:
				download_tt(title_k, pic_k, video_k)
			except:
				print ("error")	

			k = i + 1
			print(k,'/',Anum)
			



	Button(root, text="下载", width=10,command=download_all).grid(row=4, column=0, sticky=W, padx=10, pady=5)

	Button(root, text="关闭", width=10, command=root.quit).grid(row=4, column=1, sticky=E, padx=10, pady=5)

	mainloop()

if __name__ == '__main__':
    main()



