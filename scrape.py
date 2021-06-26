import requests
from bs4 import BeautifulSoup
import pprint,sys
res=requests.get('https://news.ycombinator.com/news')
soup=BeautifulSoup(res.text,'html.parser')
links=soup.select('.storylink')
subtext=soup.select('.subtext')
res=[]
soup=[]
megalinks=[]
megasubtext=[]
def num_of_pages(n):
	hn=[]
	for i in range(1,int(n)+1):
		if i==1:
			res=(requests.get('https://news.ycombinator.com/news'))
			soup=(BeautifulSoup(res.text,'html.parser'))
			megalinks=(soup.select('.storylink'))
			megasubtext=(soup.select('.subtext'))
		else:
			res=(requests.get('https://news.ycombinator.com/news'+'?p='+n))
			soup=(BeautifulSoup(res.text,'html.parser'))
			megalinks=(soup.select('.storylink'))
			megasubtext=(soup.select('.subtext'))
		hn.append(create_custom_hn(megalinks,megasubtext))
	return hn


def create_custom_hn(links,subtext):
	hn=[]
	for idx,item in enumerate(links):
		title=links[idx].getText()
		href=links[idx].get('href',None)
		votes=subtext[idx].select('.score')
		if(len(votes)):
			points=int(votes[0].getText().split(' ')[0])
			if(points>199):
				hn.append({'title':title,'link':href, 'votes':points})
	return sort_stories_votes(hn)

def sort_stories_votes(hn):
	return sorted(hn,key=lambda k:k['votes'])
hn_local=num_of_pages(sys.argv[1])
pprint.pprint(hn_local)
