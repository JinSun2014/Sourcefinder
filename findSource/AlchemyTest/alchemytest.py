import sys

from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

#for json call only
import json

def readArticle(myUrl):

    #return list
    output = {}

    response = alchemyapi.title("url", myUrl)
    output['title'] = response['title'].decode('utf8', 'ignore').encode('utf-8')

    response = alchemyapi.author("url", myUrl)
    output['author'] = response["author"].decode('utf8', 'ignore').encode('utf-8')

    #response = alchemyapi.entities("url", myUrl, { 'quotations':1 })

    #print(json.dumps(response, indent=4))

    output['people'] = GetPeople(myUrl)
    return output


#Get People, takes the url and returns all the people (and potentially data) identified in the response entities
def GetPeople(theUrl):

	#added by Xiaofeng Zhu
	responseText = alchemyapi.text('url',theUrl)

	if responseText['status'] == 'OK':
		cleanText=responseText['text'].decode('utf8', 'ignore').encode('utf-8')
	#added by Xiaofeng Zhu

	response = alchemyapi.entities("url", theUrl, { 'quotations':1 })
	person_list = []

	if response['status'] == 'OK':
		for entity in response['entities']:
			if entity['type'] == 'Person':

				#added by Xiaofeng Zhu
				personDic={}
				personDic['name'] = entity['text'].decode('utf8', 'ignore').encode('utf-8')

				person=entity['text'].encode('utf-8').replace(" ", "%20")
				personDic['twitterLink']="https://twitter.com/search?q="+person+"&src=corr&mode=users"
				personDic['linkedinLink']="https://www.linkedin.com/vsearch/p?type=people&keywords="+person
				personDic['FacebookLink']="https://www.facebook.com/search/more/?q="+person

				# personDic['subType']=""
				# if entity.get('disambiguated'):
				# 	if entity['disambiguated'].get('subType'):
				# 		personDic['subType']=entity['disambiguated']['subType'][0]

				personDic['quotation']=""
				if entity.get('quotations'):
					personDic['quotation']=entity['quotations'][0]['quotation']
				personDic['job_title']=""

				#Match job title
				location=cleanText.find(entity['text'].decode('utf8', 'ignore').encode('utf-8'))
				subText=cleanText[location-30:location+30]
				subresponse = alchemyapi.entities('text', subText, {'quotations':1 });

				if subresponse['status'] == 'OK':

					for jobentity in subresponse['entities']:
						if (jobentity['type'] =='JobTitle'):
							personDic['job_title']=jobentity['text'].decode('utf8', 'ignore').encode('utf-8')



				person_list.append(personDic)
				#added by Xiaofeng Zhu

				#removed by Xiaofeng Zhu
				# person_list.append("name: " + entity['text'])
				# if entity.get('disambiguated'):
				# 	if entity['disambiguated'].get('subType'):
				# 		person_list.append(" subType: " + entity['disambiguated']['subType'][0])
				#removed by Xiaofeng Zhu

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
