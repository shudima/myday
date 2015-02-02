#from myday_common.TextHandler import TextHandler
#from myday_common.TextScrapper import TextScrapper
#from myday_common.AnalyzedText import AnalyzedText
#from myday_common.AnalyzedTextRepository import AnalyzedTextRepository
#from myday_common.TextAnalyzer import TextAnalyzer
import json
from myday_common import *

from datetime import datetime


scrapper = TextScrapper()
analyzer = TextAnalyzer()
repository = AnalyzedTextRepository()

source = "horoscope.com"
url = 'http://my.horoscope.com/astrology/free-daily-horoscope-aries.html'
xpath = '//div[@id="textline"]'

#text = scrapper.GetText(url, xpath)

#analyzedText = analyzer.GetAnalyzedTextFromText(text)

#repository.SaveAnalyzedText(analyzedText, datetime.now(), 'libra', source, url)



#data = []
with open('config.json') as f:
    for line in f:
        data = json.loads(line)


print('OK')