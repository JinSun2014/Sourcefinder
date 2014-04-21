import sys

from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

#for json call only
import json

def readArticle(myUrl):

	#return list
	output = {}

	response = alchemyapi.title("url", myUrl)
	output['title'] = response["title"]

	response = alchemyapi.author("url", myUrl)
	output['author'] = response["author"]

	#response = alchemyapi.entities("url", myUrl, { 'quotations':1 })

	#print(json.dumps(response, indent=4))

	output['people'] = GetPeople(myUrl)
	return output


#Get People, takes the url and returns all the people (and potentially data) identified in the response entities
def GetPeople(theUrl):
	response = alchemyapi.entities("url", theUrl, { 'quotations':1 })
	person_list = []

	if response['status'] == 'OK':
		for entity in response['entities']:
			if entity['type'] == 'Person':
				person_list.append("name: " + entity['text'])
				if entity.get('disambiguated'):
					if entity['disambiguated'].get('subType'):
						person_list.append(" subType: " + entity['disambiguated']['subType'][0])
				#if entity.get('quotations'):
				#	print "Quotes: "
				#	for quote in entity['quotations']:
				#		print quote['quotation']
			#print ""
	else:
		print "Error in entity call"

	return person_list


#def GetSubtypes(Person, response_data):



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
