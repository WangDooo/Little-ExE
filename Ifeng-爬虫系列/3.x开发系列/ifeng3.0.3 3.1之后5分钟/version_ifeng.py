import urllib.request
import re


url = 'http://www.buseu.cn/version/ifeng/'

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf8')

    return html

def find_version(url):
	html = url_open(url)
	a = html.find('#')
	b = html.find('**', a, a+50)
	version = html[a+2:b]

	return version

