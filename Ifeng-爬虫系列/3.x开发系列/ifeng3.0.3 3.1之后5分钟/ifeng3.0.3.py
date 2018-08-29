import urllib.request
from version_ifeng import *
import time
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox



version_now = '3.0.0'
url = 'http://www.buseu.cn/version/ifeng/'
# standard_duration = 5
version = find_version(url)


def url_open(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
	response = urllib.request.urlopen(url)
	html = response.read()

	return html


def find_title(html):	
	a = html.find('"name": "')
	b = html.find('",', a, a+60)
	title = html[a+9:b]
	# 视频中字符处理
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

def find_pic(html):
	a = html.find('"videoLargePoster": "')
	b = html.find('",', a, a+255)
	pic = html[a+21:b]
	return pic

def find_html(html):
	# 初始化视频地址
	video_url = []
	a = html.find('<a href="')
	while a != -1:
		b = html.find('" target="_blank">', a, a+255)
		if b != -1:
			video_url.append(html[a+9:b])
		else:
			b = a + 9
		a = html.find('<a href="', b)

	return video_url

def find_video(html):
	
	a = html.find('"gqSrc":')
	b = html.find('\",', a, a+255)
	video = html[a+10:b]

	return video

def find_nowtime(html):
	
	a = html.find('class="data">')
	nowtime = html[a+13:a+32]

	return nowtime

def find_video_duration(html):
	# 初始化视频地址
	video_long = []
	a = html.find('<span>')
	while a != -1:
		b = html.find('</span>', a, a+255)
		if b != -1:
			video_long.append(html[a+6:b])
		else:
			b = a + 6
		a = html.find('<span>', b)
	return video_long

def find_endtime(html):
	
	endtime_page = []
	a = html.find('upTime">')
	while a != -1:
		b = html.find('</span>', a, a+255)
		if b != -1:
			endtime_page.append(html[a+8:b])
		else:
			b = a + 8
		a = html.find('upTime">', b)
	endtime = endtime_page[-1]
	return endtime

def timestamp_change(time_normal):
	#转换成时间数组 timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
	#转换成时间戳 timestamp = time.mktime(timeArray)
	timeArray = time.strptime(time_normal, "%Y-%m-%d %H:%M:%S") 
	timestamp_str = str(time.mktime(timeArray))
	timestamp = timestamp_str[:-2]
	return timestamp



def download_tt(title, pic, video):

	pic_suffix = pic.split('.')[-1]
	pic_name = title + '.' + pic_suffix
	video_name = title + '.mp4'

	with open(pic_name, 'wb') as f1:
		pic_t = url_open(pic)
		f1.write(pic_t)

	with open(video_name, 'wb') as f2:
		video_t = url_open(video)
		f2.write(video_t)

def write_txt(num, nowtime, video_duration, title):
	output_file = 'log.txt'
	with open(output_file, 'a', newline='',encoding="utf-8") as filewriter:
		filewriter.write(num+'. '+nowtime+' '+video_duration+' '+title+'\n')

def main():
 	 
	root = Tk()
	root.title("ifeng_v3.0.3 2018-03-01之后5分钟")
	# 禁止调整窗口大小
	root.resizable(0, 0)
	
	Label(root, text="|搞笑105|美食91|游戏172|生活140|萌萌哒101|美女85|时尚110|涨知识94|").grid()

	Label(root, text="id 分类码").grid(row=1, column=0)
	e1 = Entry(root)
	e1.grid(row=1, column=1, padx=10, pady=5)

	Label(root, text="当前时间戳(起始时间戳-反向循环)").grid(row=2, column=0)
	estring_2 = StringVar()
	e2 = Entry(root,textvariable=estring_2)
	estring_2.set('2018-03-02 12:00:00')
	e2.grid(row=2, column=1, padx=10, pady=5)

	Label(root, text="上一次时间戳(终止时间戳)").grid(row=3, column=0)
	estring_3 = StringVar()
	e3 = Entry(root,textvariable=estring_3)
	estring_3.set('2018-03-01 12:00:00')
	e3.grid(row=3, column=1, padx=10, pady=5)

	Label(root, text="设置时长 要求大于几分钟").grid(row=4, column=0)
	estring_4 = StringVar()
	e4 = Entry(root,textvariable=estring_4)
	estring_4.set(5)
	e4.grid(row=4, column=1, padx=10, pady=5)
	
	def download_all():

		if version == version_now:
			# 获取输入的值
			id_video = str(e1.get())
			time_begin = e2.get()
			time_end = e3.get()
			standard_duration = int(e4.get())
			# try:
			fname = askdirectory(title=u"选择保存到文件夹") 
			os.chdir(str(fname))
			# 输出下载到的文件夹
			print(str(fname))
			print('开始下载视频')
			# 转化为时间戳
			timestamp_begin = timestamp_change(time_begin)
			timestamp_end = timestamp_change(time_end)
			# 初始化首次结束的时间戳
			timestamp_endtime = timestamp_begin
			# 记录一共下载的视频数量
			count_video_num = 0
			# 比较当前页的最后一个视频的时间戳vs输入值 若大 则继续下载
			while int(timestamp_endtime) > int(timestamp_end):
				video_addrs = []
				video_duration = []
				nowtime = '1'
				url = 'http://v.ifeng.com/vlist/channel/'+id_video+'/'+timestamp_begin+'000/25/channel_more.js'			
				# 找到html
				html = url_open(url).decode('utf8')
				video_addrs = find_html(html)
				# 得到视频时长
				video_duration = find_video_duration(html)
				# js 页面的视频数 24
				num_video_24 = len(video_addrs)
				# 找到当前页面的最后一个视频的时间戳
				endtime = find_endtime(html)
				timestamp_endtime = timestamp_change(endtime)				
				# 循环下载js中的视频
				for i in range(num_video_24):
					# 得到该视频时长 
					duration_k = video_duration[i]
					# 取第二位
					video_duration_compare = int(duration_k[:2])
					if video_duration_compare >= standard_duration:
						# 读取每个视频地址
						url_api = video_addrs[i]
						# 编码utf8
						html = url_open(url_api).decode('utf8')
						# 得到该视频发布时间
						nowtime = find_nowtime(html)
						# 得到该视频名称
						title_k = find_title(html)
						# 得到该视频封面
						pic_k = find_pic(html)
						# 得到该视频
						video_k = find_video(html)
						# 下载视频
						try:
							download_tt(title_k, pic_k, video_k)
						except:
							print ("error")
						# 记录当前下载视频总数
						count_video_num += 1
						# 输出下载信息
						write_txt(str(count_video_num),nowtime,duration_k,title_k)
						print(str(count_video_num)+'.',nowtime,duration_k,title_k)	

				# 当前最后一个视频的时间戳 变为下一个js的起始时间
				timestamp_begin = timestamp_endtime
			# except:
			# 	tkinter.messagebox.showinfo('提示', '错误')
			print('Done')
		else:
			tkinter.messagebox.showinfo('提示', '请更新到最新版本')
			sys.exit(0)


	Button(root, text="下载", width=10, command=download_all).grid(row=6, column=0, sticky=W, padx=10, pady=5)

	Button(root, text="关闭", width=10, command=root.quit).grid(row=6, column=1, sticky=E, padx=10, pady=5)

	mainloop()


if __name__ == '__main__':
    main()