from bs4 import BeautifulSoup
import requests
import urllib.request
from inscriptis import get_text

try: 
	from googlesearch import search 
except ImportError: 
	print("No module named 'google' found") 

# to search 
query = input()

for j in search(query, tld="com", num=10, stop=10,pause=2): 
      r = requests.get(j)
      html_content = r.text
      soup = BeautifulSoup(html_content,'lxml')
      html = urllib.request.urlopen(j).read().decode('utf-8')
      word_find = get_text(html)
      print("URL is : ")
      if "wikipedia" in j and "Wikipedia" in soup.title.string :
          print(j)
      x=query.split()
      y=str(word_find).split()
      c=0
      frequency=[]
      for i in x :
         for j in y :
              if i in j :
                   c=c+1
         frequency.append(c)
         c=0
      print('frequency of words in given web page are : ')
      for i in range(0,len(frequency)):
            print("frequency of "+x[i]+" is : "+str(frequency[i]))