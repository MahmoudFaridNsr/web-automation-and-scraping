import requests
from BotStructures import Item
from bs4 import BeautifulSoup
class PageScraper:
	def extract_discount(self,span): #convert span into discount value
		span=str(span)
		ret = ""
		started = False
		for i in range(1,len(span)):
			if span[i+1] =='%':
				break
			if span[i] =='>':
				started=True
				continue
			if started ==True:
				ret= ret + span[i]
		return ret		

			
	def page_scraper(self,url):
		items=[]
		item = Item()
		self.url = url
		res = requests.get(url)
		html_page = str(res.content)
		# stopping the handler looping from getting more end pages
		if (html_page.count('not found results for'))==1:
			print("Bad Page [ Stopped Scraping this Category] URL = "+url) 
			return -1
		soup = BeautifulSoup(html_page, 'html.parser')
		#print("Started ...")
		divTag = soup.find_all("div",{"class":"column column-block block-list-large single-item"})
		for tag in divTag:
			#tdTags = tag.find_all('span',{"class":"discount"})
			#for ele in tdTags:
			#	print(ele)
			tdTags = tag.find_all('span', {'class' :'discount'})
			if len(tdTags)==0:
				continue
			tdTags = PageScraper.extract_discount(self,tdTags[0])
			#print(tdTags) #offer
			item.offer = tdTags
			#print("++++")
			tdTags = tag.find('div', {'class' :'is sk-clr1'}).find('h3').text
			#print(tdTags) # price
			item.price = tdTags
			#print("++++")
			item.desc = tag.get('data-name') #descripe
			#print("****")
			tdTags = tag.find_all('a',{"class":"img-bucket img-link itemLink sPrimaryLink"},href=True)
			for ele in tdTags:
				item.link =ele.get('href')
			#	print(ele.get('href')) #link
				#print("++++")
			tdTags = tag.find_all('img',{"class":"img-size-medium lazy-loaded imageUrl"},src=True)
			for ele in tdTags:
				item.img =ele.get('src')
				#print(ele.get('src'))	#img
				#print('-------------------')
			items.append(item)	
			#print(item)	
		#print("Done.....")
		return items
		

#page_scraper()
#print(text[1])


#print(output)2