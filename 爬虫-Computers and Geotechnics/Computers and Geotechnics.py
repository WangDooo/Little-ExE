# https://www.sciencedirect.com/journal/computers-and-geotechnics/
import csv
from bs4 import BeautifulSoup
from HandleJs import Py4Js 
import urllib.request  


def open_url(url):    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}      
    req = urllib.request.Request(url = url,headers=headers)    
    response = urllib.request.urlopen(req)    
    data = response.read().decode('utf-8')    
    return data 



def translate(content,tk):    
    if len(content) > 4891:    
        print("翻译的长度超过限制！！！")    
        return     
        
    content = urllib.parse.quote(content)    
        
    url = "http://translate.google.cn/translate_a/single?client=t"+ "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca"+"&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1"+"&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s"%(tk,content)    
        
    #返回值是一个多层嵌套列表的字符串形式，解析起来还相当费劲，写了几个正则，发现也很不理想，  
    #后来感觉，使用正则简直就是把简单的事情复杂化，这里直接切片就Ok了    
    result = open_url(url)    
        
    end = result.find("\",")    
    if end > 4:    
        return result[4:end]

def translate_title(title_list):
	title_chn_list = []
	for each in title_list:
		js = Py4Js()
		tk = js.getTk(each)
		title_chn = translate(each,tk)
		title_chn_list.append(title_chn)
	return title_chn_list



def main():
	with open('Computers and Geotechnics _ Vol 93.html','r',encoding='utf-8') as f:
		html = f.read()
		soup = BeautifulSoup(html, 'lxml')

		title_list = []
		href_list = []
		title_chn = []

		title = soup.find_all("span", class_="js-article-title")
		for each in title:
			title_list.append(each.get_text())
		href = soup.find_all("a", class_="anchor pdf-download u-margin-l-right text-s")
		for each in href:
			href_list.append(each['href'])
		title_chn = translate_title(title_list)


	output_file = 'output.csv'
	num = 1
	vol = 107

	with open(output_file,'w',newline='') as csv_out_file:
		filewriter = csv.writer(csv_out_file)
		filewriter.writerow(['序号','Vol','Title','题目','网址'])
		for i in range(len(title_list)):
			filewriter.writerow([num,vol,title_list[i], title_chn[i], href_list[i]])
		
        
if __name__ == "__main__":    
    main() 
