import scrapy
from textblob import TextBlob


class HoroscopeComSpider(scrapy.Spider):
	name = "HoroscopeCom"
	allowed_domains = ['horoscope.com']

	start_urls = ['http://my.horoscope.com/astrology/free-daily-horoscope-libra.html']


	def parse(self, response):
		for sel in response.xpath('//div[@id="textline"]'):
			horoscopeText = sel.xpath('text()').extract()

			text = ''.join(horoscopeText)
			blob = TextBlob(text)


			polarity_sum = 0.0;
			count = 0;

			for sentence in blob.sentences:
				polarity_sum = polarity_sum + sentence.sentiment.polarity
				count = count + 1;


			polarity_avg = polarity_sum / count

			print(horoscopeText)
			print(polarity_avg)
			print(blob.noun_phrases)
			