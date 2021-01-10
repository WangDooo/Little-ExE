import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

# POST发送到的网址
url_login = "https://newids.seu.edu.cn/authserver/login"
url_login_info = "https://newids.seu.edu.cn/authserver/login"
url_login_pwd = "https://newids.seu.edu.cn/authserver/needCaptcha.html?username=230198118&pwdEncrypt2=LQ8ws6C2MCQrXKAygpi1vwlZohJnK6ezN4V3vnqGNsq9tdi7mRE7SjCAV+RN+2aUGNI8y4Op6dr8mMQU1Pn76L8YsJa4SinPjwkcP7eM6X0=&_=1610271193108"
# 想要爬取的登录后的页面  
url_after =  "https://newids.seu.edu.cn/authserver/index.do"
url_after2 = "http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index.do#/dailyReport"
url_after3 = "https://seicwxbz.seu.edu.cn/self-service/?ticket=ST-zzj-64d690fb16844991b97b89fd830fb2d1-cas"

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}


s = requests.session()

# login = s.get(url_login, headers = headers)
# print('login.cookies =',login.cookies)
# print(s.cookies.get_dict())
cookie_str = r"route=249cb391d30fa3e46a1009b55ebd85fc; gr_user_id=e3ba5071-134e-4e54-905b-459ead50ff9c; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; zg_=%7B%22sid%22%3A%201606273697471%2C%22updated%22%3A%201606273697475%2C%22info%22%3A%201606273697474%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22ehall.seu.edu.cn%22%2C%22cuid%22%3A%20%22230198118%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201606273697471%7D; zg_did=%7B%22did%22%3A%20%22172bc0cd94218a-0e71b030be046d-7373667-1fa400-172bc0cd943efa%22%7D; zg_8da79c30992d48dfaf63d538e31b0b27=%7B%22sid%22%3A%201609213965328%2C%22updated%22%3A%201609214075848%2C%22info%22%3A%201609213965331%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201609213965328%7D; JSESSIONID=fZDrpbeXD7cpHxhI1PhDw_ej3imVJ7xktNT3aubkKNDrZAaJLVEP!-543703607"
cookies = {}
for line in cookie_str.split(';'):
	key, value = line.split('=', 1)
	cookies[key] = value

response = s.get(url_after2, cookies = cookies,headers = headers)
print(response.content.decode('utf-8'))

"""

def login(par1,afterURL,loginURL):
	s = requests.session()  
	login = s.post(loginURL, data = par1, headers = headers)                  # 发送登录信息，返回响应信息（包含cookie）  
	response = s.get(afterURL, cookies = login.cookies, headers = headers)    # 获得登陆后的响应信息，使用之前的cookie  
	print(login.cookies)
	return response.content.decode('utf-8')  

# https://newids.seu.edu.cn/authserver/needCaptcha.html?username=230198118&pwdEncrypt2=pwdEncryptSalt&_=1610266719864


data1 = r'username=230198118&password=4Dp5nN9t%2Balv9cPDDUgcccO22Eoylf7ebIDPvBz7X0UtN17Vq4%2F%2FTzxRbpRefG6Nt7RkRP%2BoTzlG7klB%2Fuk8D%2BIckUpaoFon67QIj7NNNBA%3D&lt=LT-2361028-HWjNmXt4fza3mUnXqsq937MntlP4Vr1610267306876-dEbo-cas&dllt=userNamePasswordLogin&execution=e1s3&_eventId=submit&rmShown=1'
data2 = r'username=230198118&password=4Dp5nN9t%2Balv9cPDDUgcccO22Eoylf7ebIDPvBz7X0UtN17Vq4%2F%2FTzxRbpRefG6Nt7RkRP%2BoTzlG7klB%2Fuk8D%2BIckUpaoFon67QIj7NNNBA%3D'
data_josn = {}
for line in data2.split('&'):
	key, value = line.split('=', 1)
	data_josn[key] = value

# print('data_josn =',data_josn)

# print(login(par1=data_josn,afterURL=url_after,loginURL=url_login))





#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'route=249cb391d30fa3e46a1009b55ebd85fc; gr_user_id=e3ba5071-134e-4e54-905b-459ead50ff9c; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; zg_=%7B%22sid%22%3A%201606273697471%2C%22updated%22%3A%201606273697475%2C%22info%22%3A%201606273697474%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22ehall.seu.edu.cn%22%2C%22cuid%22%3A%20%22230198118%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201606273697471%7D; zg_did=%7B%22did%22%3A%20%22172bc0cd94218a-0e71b030be046d-7373667-1fa400-172bc0cd943efa%22%7D; zg_8da79c30992d48dfaf63d538e31b0b27=%7B%22sid%22%3A%201609213965328%2C%22updated%22%3A%201609214075848%2C%22info%22%3A%201609213965331%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201609213965328%7D; JSESSIONID=KrLre-bjVLP_1RPUtc1fAV4tnkfBy_XriXreQ4oQjaal0sVvb5gI!-543703607'


#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
	key, value = line.split('=', 1)
	cookies[key] = value

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

#在发送get请求时带上请求头和cookies
resp = requests.get(url_after, headers = headers, cookies = cookies)

print(resp.content.decode('utf-8'))
"""