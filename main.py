import urllib2
import re
import time

def get_urls(url_):
	pattern = re.compile(r'publish/thunews/.*?\.html')
	request = urllib2.Request(url_)
	try:
		response = urllib2.urlopen(request)
		time.sleep(0.05)
	except urllib2.URLError, e:
		print e.reason
		return []
	list_ = re.findall(pattern, response.read())
	return list_

import Queue

initial_page = "http://news.tsinghua.edu.cn/publish/thunews/index.html"

url_queue = Queue.Queue()
seen = set()

seen.add(initial_page)
url_queue.put(initial_page)

cnt = 0 

f=file("urls.txt","w")

while (True):
	if url_queue.empty() == False:
		current_url = url_queue.get()
		cnt = cnt + 1
		f.write(current_url+'\n')
		print cnt, ':', current_url
		urls = get_urls(current_url)
		for next_url in urls:
			actual_url = "http://news.tsinghua.edu.cn/" + next_url
			if actual_url not in seen:
				seen.add(actual_url)
				url_queue.put(actual_url)
	else:
		break
