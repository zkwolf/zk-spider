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
		print(format_now)
		self.requests.keep_alive = False
		postfix = '/?_trans_=000019_jrjs_sy'
		data = self.requests.get(self.page + postfix, headers=self.headers)
		# if data.status_code == 200:
		# 	location = data.headers['Location']
		# 	data = self.requests.get(location, headers=self.headers)
		soup = BeautifulSoup(data.text, 'html.parser')
		os.chdir(curr_dir + self.directory)
		os.makedirs(format_now, exist_ok=True)
		os.chdir(format_now)
		os.makedirs('css', exist_ok=True)
		os.makedirs('js', exist_ok=True)
		os.makedirs('image', exist_ok=True)
		os.chdir('css')
		css = soup.find_all('link', attrs = {'type'= 'text/css'})
		for i in css:
			css_data = self.requests.get(i['href'], headers=self.headers)
			_, name = os.path.split(i['href'])
			with open(name, 'wb') as f:
				f.write(css_data.text.encode('utf-8'))
			i['href'] = 'css/' + name
		os.chdir('../js')
		js = soup.find_all('script', attrs = {'type'= 'text/javascript'})
		for i in js[1:]:
			js_data = self.requests.get(i['src'], headers=self.headers)
			_, name = os.path.split(i['src'])
			with open(name, 'wb') as f:
				f.write(js_data.text.encode('utf-8'))
			i['src'] = 'js/' + name
		os.chdir('../image')
		image = soup.find_all('img')
		for i in image:
			image_data = self.requests.get(i['src'], headers=self.headers)
			_, name = os.path.split(i['src'])
			with open(name, 'wb') as f:
				f.write(image_data.content)
			i['src'] = 'image/' + name
			
		os.chdir(..)
		with open('index.html', 'wb') as f:
			f.write(soup.encode('utf-8'))
		os.chdir(curr_dir)

	def run(self):
		while True:
			self.get_data()
			time.sleep(self.interval)
			
if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('-d', type=int, help='Set time interval')
	parser.add_argument('-u', help="Set page address")
	parser.add_argument('-o', help="Set save file")

	args = parser.parse_args()
	#['-d', '60', '-u', 'http://m.sohu.com', '-o', '/tmp/backup']
	getpage = GetPage()
	getpage.run()