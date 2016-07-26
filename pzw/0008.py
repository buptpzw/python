import urllib2
from bs4 import BeautifulSoup

request = urllib2.Request("http://www.jianshu.com/p/b23583bf1296")
response = urllib2.urlopen(request)
html = response.read()

soup = BeautifulSoup(html,"html.parser")
p = soup.find("div",class_="show-content")
content = p.get_text()

print content
