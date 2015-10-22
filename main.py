import argparse
import requests
from bs4 import BeautifulSoup
import time
import datetime
import os
parser = argparse.ArgumentParser()

parser.add_argument('-d', type=int, help='Set time interval')
parser.add_argument('-u', help="Set page address")
parser.add_argument('-o', help="Set save file")

args = parser.parse_args()

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
		now = datetime.datetime.now()
		format_now = now.strftime('%Y%m%d%H%M')
		temp = self.requests.get(self.page, headers=self.headers) 
		# the temp to get redirect url
		data = self.requests.get(temp.url, headers=self.headers)
		with open('index.html', 'wb') as f:
			f.write(data.text.encode('utf-8'))

if __name__ == "__main__":
	getpage = GetPage()
	getpage.get_data()


