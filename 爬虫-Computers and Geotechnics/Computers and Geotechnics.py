import urllib.request
import csv

def url_open(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
	response = urllib.request.urlopen(url)
	html = response.read()

	return html


# html = url_open(url).decode('utf8')


output_file = 'output.csv'

test = [123,123,123]
english = ['one','two','three']

with open(output_file,'w',newline='') as csv_out_file:
	filewriter = csv.writer(csv_out_file)
	for i in range(len(test)):
		temp = []
		temp.append(test[i])
		temp.append(english[i])
		filewriter.writerow(temp)
	