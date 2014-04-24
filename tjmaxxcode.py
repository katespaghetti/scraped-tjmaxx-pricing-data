import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://tjmaxx.tjx.com/store/jump/category/handbags/departments/view-all/cat630008p"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

req = urllib2.Request(url, headers=hdr)

response = urllib2.urlopen(req)
#print response.read()

html = response.read()
parsed_html = BeautifulSoup(html)

product_attributes = parsed_html.body.findAll('div', attrs={'class':'product'})

for element in product_attributes:
	product_brand = element.find('span', attrs={'class':'product-brand'})

	if product_brand:
		product_brand = product_brand.text
	else: 
		product_brand = ""

	product_title = element.find('span', attrs={'class':'product-title'})
	
	if product_title:
		product_title = product_title.text
	else:
		product_title = ""

	price_comparison = element.find('span', attrs={'class':'price-comparison'}).text
	product_price = element.find('span', attrs={'class':'product-price'}).text

	print element["id"], product_brand, product_title, price_comparison, product_price

print len(product_attributes)

#for price in product_attributes:
#	print price.text