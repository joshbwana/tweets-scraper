import urllib
import urllib.request
from bs4 import BeautifulSoup
print("Enter your Twitter Username")
d = input()
theurl = "https://twitter.com/{j}".format(j=d)
thepage =urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")
print(soup.title.text)
""" for link in soup.findAll('a'):
        print(link.get('href')
        print(link.text)
        """
print(soup.find('div', {"class":"ProfileHeaderCard"}).find('p').text)
i = 1
for tweets in soup.findAll('div', {"class":"content"}):
                print("TWEET NUMBER :", i)
                print("\n")
                print(tweets.find('p').text)
                i = i+1
