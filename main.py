from myday_common.TextHandler import TextHandler
from myday_common.TextScrapper import TextScrapper
from myday_common.AnalyzedText import AnalyzedText
from myday_common.AnalyzedTextRepository import AnalyzedTextRepository
from myday_common.TextAnalyzer import TextAnalyzer
import json
import os
import sys
from threading import Thread
from datetime import datetime


def GetSources():
	script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
	rel_path = 'myday_config/sources.json'
	abs_file_path = os.path.join(script_dir, rel_path)
	with open(abs_file_path) as data_file:    
		data = json.load(data_file)
    	return data

def GetSigns():
	script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
	rel_path = 'myday_config/signs.json'
	abs_file_path = os.path.join(script_dir, rel_path)
	with open(abs_file_path) as data_file:    
		data = json.load(data_file)
    	return data


def ScrapAndSave(url, xpath, sign, source):
	try:
		scrapper = TextScrapper()
		analyzer = TextAnalyzer()
		repository = AnalyzedTextRepository()

		print('Scrapping ' + sign + ' from ' + source)
		text = scrapper.GetText(url, xpath)

		print('Analyzing ' + sign + ' from ' + source)
		analyzedText = analyzer.GetAnalyzedTextFromText(text) 

		print('Saving ' + sign + ' from ' + source)
		repository.SaveAnalyzedText(analyzedText, datetime.now(), sign, source, url)

	except Exception as e:
		print("Unexpected error saving " + url + " error:" + str(e) + '\n')
		pass


def Main():
	sources = GetSources()
	signs = GetSigns()

	threads = []

	# For each source, url and sign, start scrapping thread
	for source in sources:
		for url in source['urls']:
			for sign in signs.values():

				try:

					the_url = url['url'] %sign
					xpath = url['xpath']
					the_source = source['name']
					t = Thread(target=ScrapAndSave, args=(the_url,xpath,sign,the_source,)) 
					t.start()
					threads.append(t)
				except Exception as e:
					print("Unexpected error loading configuration for " + url + " error:" + str(e) + '\n')
					pass

	# Wait for threads to finish
	i =0
	for t in threads:
		t.join()
		i = i + 1
		print('Done %d out of %d' % (i, len(threads)))




Main()
print('Ok')
