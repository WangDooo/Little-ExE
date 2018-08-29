import urllib.request
import os
import re

global video_addrs, imgs_addrs, title

video_addrs = []

def find_html(html):
	
	a = html.find('<li><a href="')
	
	while a != -1:
		b = html.find('" target="_blank"', a, a+255)
		if b != -1:
			video_addrs.append(html[a+13:b])
		else:
			b = a + 13

		a = html.find('<li><a href="', b)

	for each in video_addrs:
		print(each)
	return video_addrs


with open('1.txt', encoding='utf-8',errors='ignore') as f:
	html = f.read()
	find_video(html)
	print(len(video_addrs))
