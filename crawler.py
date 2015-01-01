import requests  
from lxml import html  
import sys  
import urlparse
import collections

STARTING_URL = 'http://www.goal.com/en-ie'

urls_queue = collections.deque()
urls_queue.append(STARTING_URL)
found_urls = set()
found_urls.add(STARTING_URL)

while len(urls_queue):
	url = urls_queue.popleft()
	response = requests.get(url)
	parsed_body = html.fromstring(response.content)
	
	# print the page title
	print parsed_body.xpath('//title/text()')
	
	links = [urlparse.urljoin(response.url, url) for url in parsed_body.xpath('//a/@href')]
	for link in links:
		found_urls.add(link)
		if url not in found_urls and url.startswith('http'):
			urls_queue.add(link)



