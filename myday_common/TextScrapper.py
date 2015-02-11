from lxml import html 
import requests

AGENT =  'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


class TextScrapper:

	def GetText(self, url, xpath):

		user_agent = {'User-agent': AGENT}
		response  = requests.get(url, headers = user_agent, timeout=5)
		tree = html.fromstring(response.text.encode('utf-8'))
		textDiv = tree.xpath(xpath)

		text = textDiv[0].text
		
		return text


