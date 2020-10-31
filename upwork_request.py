from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
from time import sleep
import requests
from random import randint

# session = HTMLSession()
session = requests.Session()
job = 1
def scrape(url):
	global job
	global session

	cookies = {'Cookie': 'G_AUTHUSER_H=0; visitor_id=197.235.58.62.1600403004618029; G_ENABLED_IDPS=google; _pxhd=6c481f721bd2e32693c8a6b339191d9410a08546c900e6f6d63d0cb54ed417c9:afe64ed1-f969-11ea-93d2-193c12f06740; recognized=christiangudo017; company_last_accessed=d33542524; current_organization_uid=1284918021448695810; __cfruid=27f36733c46bae7bce6bdc9e83194640a73a5b5e-1604004344; XSRF-TOKEN=77b803a9f96733bc2305db7e190f676c; channel=direct; session_id=5d17d535505c7f74b1afbd6220bc110e; __cfduid=d63d1024d24e93cbc23a34014ea92b57a1604004278; device_view=full; cdContextId=2; cdContextId=2; bmuid=1604004468274-2FA9BBB9-26E3-478B-BD04-C3D9952A8C66; upwork_bc=1604004468290_197.235.58.62.1600403004618029; cdSNum=1604004466853-sjn0000368-55095c1e-09be-4d5e-a0e8-ac2b00bae6be'}
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:79.0) Gecko/20100101 Firefox/79.0'}

	r = session.get(url, headers=headers, cookies=cookies)
	# r.html.render()
	html = r.text.encode('utf-8')
	# html = html.decode('ascii', 'ignorsecse')

	soup = BeautifulSoup(html, 'lxml')
	titulos = soup.find_all('a', {'class': 'job-title-link break visited'})

	for titulo in titulos:
		href = titulo.get('href')
		link = f'https://www.upwork.com{href}'
		print(titulo.getText().strip().replace('\n', ''))
		print(link)
		print('')

	sleep(randint(5,15))

	def eachjob():
		global job
		for titulo in titulos:
			href = titulo.get('href')
			r = session.get(f'https://www.upwork.com{href}', headers=headers, cookies=cookies)
			# r.html.render()

			print('-=' * 70)
			print(f'JOB {job}: https://www.upwork.com{href}')
			print('-=' * 70)
			job += 1

			html = r.text.encode('utf-8')
			html = html.decode('ascii', 'ignore')
			soup = BeautifulSoup(html, 'lxml')
			sections = soup.find_all('section', class_='up-card-section')

			for section in sections:
				print(section.getText().strip().replace('\n', ''))
				print()

			sleep(randint(5,15))
	eachjob()

scrape('https://www.upwork.com/ab/jobs/search/?proposals=0-4&q=bot&sort=recency')
page = 2
while page <= 3:
	scrape(f'https://www.upwork.com/ab/jobs/search/?page={page}&proposals=0-4&q=bot&sort=recency')
	page += 1
	