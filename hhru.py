import requests
from bs4 import BeautifulSoup as bs
import lxml
import os
import django
import schedule
import time
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello.settings')
django.setup()
from table.models import Table


def hhru_parse ():
	jobs = []
	urls = []
	headers = {'accept' : '*/*' , 'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' }
	base_url = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&text=python&page=0'
	urls.append(base_url)
	session = requests.Session()
	request = session.get(base_url, headers = headers)
	if request.status_code == 200:
		soup = bs(request.content, 'lxml')
		try:
			pagination = soup.find_all('a', attrs = {'data-qa' : 'pager-page'})
			count= 1 # int(pagination[-1].text)
			for i in range(count):
				url = f'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&text=python&page={i}'
				if url not in urls:
					urls.append(url)
		except:
			pass
		
		for url in urls:
			request = session.get(url, headers = headers)
			soup = bs(request.content, 'lxml')
			divs = soup.find_all('div', attrs = {'data-qa' : 'vacancy-serp__vacancy'})
			for div in divs:
				try:
					title = div.find('a', attrs = {'data-qa' : 'vacancy-serp__vacancy-title'}).text
					link = div.find('a', attrs = {'data-qa' : 'vacancy-serp__vacancy-title'})['href']

					
					for i in div:
						request = session.get(link, headers = headers)
						soup = bs(request.content, 'lxml')
						c_name = soup.find('p', attrs = {'data-qa' : 'vacancy-contacts__fio'})
						if c_name != None:
							name = c_name.text
						else:
							name = 'empty'
						
						c_number = soup.find('p', attrs={'data-qa' : 'vacancy-contacts__phone'})
						if c_number != None:
							number = c_number.text
						else:
							number = 'empty'
						
						
						c_email = soup.find('p', attrs={'data-qa' : 'vacancy-contacts__email'})
						if c_email != None:
							email = c_email.text
						else:
							email = 'empty'
						
						c_address = soup.find('span', attrs={'data-qa' : 'vacancy-view-raw-address'})
						if c_address != None:
							address = c_address.text
						else:
							address= 'empty'
							
						date_public = soup.find('meta', attrs={'itemprop' : 'datePosted'})['content']
						date = date_public.split('T')
						now = datetime.datetime.now()
						today = str(now.date())
						
					
					if date[0] == today:
						employer = Table()
						
						employer.title = title
						employer.link = link
						employer.name = name
						employer.number = number
						employer.email = email
						employer.address = address
						employer.date_public = date_public
						employer.save()
					else:
						pass
					
				    
						
					   
					#jobs.append({'title' : title, 'link' : link, 'name' : name, 'number' : number, 'email' : email, 'address' : address, 'date_public' : date_public})
					
				   
					
					
					

				except:
					pass

	else:
		print('error')
'''	
		
schedule.every().day.at('23:10').do(hhru_parse)
	
while True:
	schedule.run_pending()
	time.sleep(1)	
'''

hhru_parse()
