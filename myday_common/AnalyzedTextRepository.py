from pymongo import MongoClient

MONGO_HOST = 'mongodb://admin:admin@ds031691.mongolab.com:31691/shudima'

class AnalyzedTextRepository:
	def SaveAnalyzedText(self, analyzedText, date, sign, source, url):

		text_object = self.CreateTextObjet(analyzedText, date, sign, source, url, type)

		client = MongoClient(MONGO_HOST)
		
		db = client.shudima

		texts = db.analyzed_texts

		texts.insert(text_object)


	def CreateTextObjet(self, analyzedText, date, sign, source, url):

		text_object = {}
		text_object['text'] = analyzedText.text
		text_object['sentiment'] = analyzedText.sentiment
		text_object['words'] = analyzedText.words
		text_object['date'] = date.strftime('%m/%d/%Y')
		text_object['sign'] = sign
		text_object['source'] = source
		text_object['url'] = url

		return text_object
		