from bs4 import BeautifulSoup
import urllib.request

url = 'https://altin.in/fiyat/gram-altin/ziraat'
urlopen = urllib.request.urlopen(url)

soup = BeautifulSoup(urlopen, 'html.parser')

buying = soup.find('li', class_='midrow alis').text
sales = soup.find('li', class_='midrow satis').text

print('Alış: ' + str(buying))
print('Satış: ' + str(sales))
