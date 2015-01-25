import scrapy

class HoroscopeComSpider(scrapy.Spider):
	name = "HoroscopeCom"
	allowed_domains = ['horoscope.com']

	start_urls = ['http://my.horoscope.com/astrology/free-daily-horoscope-libra.html']


	def parse(self, response):
		print('Response')