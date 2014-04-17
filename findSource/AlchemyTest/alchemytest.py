import sys

from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

#for json call only
import json

def readArticle(myUrl):

	#return list
	output = [];

	#early test
	#myText = "What do you think about doing this on Saturday?"
	#response = alchemyapi.sentiment("text", myText)
	#print "Sentiment: ", response["docSentiment"]["type"]

	#myUrl = sys.argv[1]

	response = alchemyapi.title("url", myUrl)
	output.append("Title: " + response["title"])

	response = alchemyapi.author("url", myUrl)
	output.append("Author: " + response["author"])

	response = alchemyapi.entities("url", myUrl, { 'quotations':1 })

	#print(json.dumps(response, indent=4))


	if response['status'] == 'OK':
		for entity in response['entities']:
			output.append("Text: " + entity['text'] + "\n Type: " + entity['type'])
			if entity.get('quotations'):
				print "Quotes: "
				for quote in entity['quotations']:
					print quote['quotation']
			print ""
	else:
		print "Error in entity call"

	print ""
	print "Concepts"
	print ""
	response = alchemyapi.concepts('url', myUrl)
	if response['status'] == 'OK':
		for concept in response['concepts']:
			print "Text: ", concept['text']
			print ""
	else:
		print "Error in concept call"

	return output

	# print ""
	# print "Keywords"
	# print ""
	# response = alchemyapi.keywords('url', myUrl, { 'sentiment': 1})
	# if response['status'] == 'OK':
	# 	for keyword in response['keywords']:
	# 		print "Text: ", keyword['text']
	# 		print ""
	# else:
	# 	print("Error in Keyword extraction")
