from bs4 import BeautifulSoup
import urllib2
krsNumber = '0000056901'
query = 'https://api.mojepanstwo.pl/krs/podmioty?conditions[krs]=' + str(krsNumber)
print(query)
response = urllib2.urlopen('https://api.mojepanstwo.pl/krs/podmioty?conditions[krs]=' + str(krsNumber))

html = response.read()
print(html)
