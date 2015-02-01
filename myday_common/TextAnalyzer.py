from textblob import TextBlob
from myday_common.AnalyzedText import AnalyzedText

class TextAnalyzer:
	def GetAnalyzedTextFromText(self, text):
		blob = TextBlob(text)

		polarity_sum = 0.0;
		count = 0;

		for sentence in blob.sentences:
			polarity_sum = polarity_sum + sentence.sentiment.polarity
			count = count + 1;


		polarity_avg = polarity_sum / count

		return AnalyzedText(text, polarity_avg, blob.noun_phrases)