from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

#for json call only
import json

myText = "What do you think about doing this on Saturday?"
response = alchemyapi.sentiment("text", myText)
print "Sentiment: ", response["docSentiment"]["type"]

myUrl = "http://news.yahoo.com/sebelius-health-care-launch-terribly-flawed-145354241--finance.html"

response = alchemyapi.title("url", myUrl)
print "Title: ", response["title"]

response = alchemyapi.author("url", myUrl)
print "Author: ", response["author"]

response = alchemyapi.entities("url", myUrl, { 'quotations':1 })

print(json.dumps(response, indent=4))


if response['status'] == 'OK':
	for entity in response['entities']:
		print "Text: ", entity['text']
		print "Type: ", entity['type']
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
