import argparse
import requests
from bs4 import BeautifulSoup
import time
import datetime
import os


class GetPage:

	def __init__(self):
		self.interval = args.d
		self.page = args.u
		self.directory = args.o
		self.requests = requests
		self.headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'
						}

	def get_data(self):
		curr_dir = os.getcwd().replace('\\', '/')
		os.makedirs(curr_dir + self.directory, exist_ok=True)
		now = datetime.datetime.now()
		format_now = now.strftime('%Y%m%d%H%M')
		request = self.requests
		request.keep_alive = False
		temp = request.get(self.page, headers=self.headers)
		# the temp to get redirect url
		data = request.get(temp.url, headers=self.headers)
		soup = BeautifulSoup(data.text, 'html.parser')
		os.chdir(curr_dir + self.directory)
		os.makedirs(format_now, exist_ok=True)
		os.chdir(format_now)
		with open('index.html', 'wb') as f:
			f.write(data.text.encode('utf-8'))
		os.makedirs('css')
		os.makedirs('js')
		os.makedirs('image')
		os.chdir('css')
		css = {x.attrs.get('href') for x in soup.select('link[type="text/css"]')}
		for i in css:
			if i:
				css_data = request.get(i, headers=self.headers)
				_, name = os.path.split(i)
				with open(name, 'wb') as f:
					f.write(css_data.text.encode('utf-8'))
		os.chdir('../js')
		js = {x.attrs.get('src') for x in soup.select('script[type="text/javascript]')}
		for i in js:
			if i:
				js_data = request.get(i, headers=self.headers)
				_, name = os.path.split(i)
				with open(name, 'wb') as f:
					f.write(js_data.text.encode('utf-8'))
		os.chdir('../image')
		image = {x.attrs.get('src') for x in soup.select('img')}
		for i in image:
			if i:
				image_data = request.get(i, headers=self.headers)
				_, name = os.path.split(i)
				with open(name, 'wb') as f:
					f.write(image_data.text.encode('utf-8'))


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('-d', type=int, help='Set time interval')
	parser.add_argument('-u', help="Set page address")
	parser.add_argument('-o', help="Set save file")

	args = parser.parse_args(['-d', '60', '-u', 'http://m.sohu.com', '-o', '/tmp/backup'])
	getpage = GetPage()
	getpage.get_data()
	


