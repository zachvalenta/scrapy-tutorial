import scrapy

file = 'books.txt'

class ZVIntroSpider(scrapy.Spider):
	name = "zv-intro"

	urls = [
		'http://books.toscrape.com/catalogue/page-1.html',
		'http://books.toscrape.com/catalogue/page-2.html',
		'http://books.toscrape.com/catalogue/page-3.html',
		'http://books.toscrape.com/catalogue/page-4.html',
		'http://books.toscrape.com/catalogue/page-5.html'
	]

	for url in urls:
		yield scrapy.Request(url=url, callback=self.parse)


	def parse(self, response):
		book_list = response(css.'article.product_pod > h3 > a::attibute(title)').extract()

		with open(file, 'a+') as f:
			for title in titles:
				f.write(title + '\n')
