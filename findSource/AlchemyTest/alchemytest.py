import sys

from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

#for json call only
import json

def readArticle(myUrl, original_source):

    output = {}
    response = alchemyapi.title("url", myUrl)
    response_a = alchemyapi.author("url", myUrl)
    output['author'] = response_a["author"].encode('utf-8', 'ignore')
    if output['author'] =='':
    	output['author'] = 'anonym'


    output['people'] = GetPeople(myUrl)
    if (len(output['people'])==0):
    	output={}
    else:
    	output['url'] = myUrl
    	output['original_source'] = original_source

    	output['title'] = response['title'].encode('utf-8', 'ignore')
    	if output['title'] =='':
    		output['title']='No title found'
	
    return output


#Get People, takes the url and returns all the people (and potentially data) identified in the response entities
def GetPeople(theUrl):
	person_list_dict = {}

	people_response = alchemyapi.entities("url", theUrl, { 'quotations':1 })

	name_quotation={}
	if people_response['status'] == 'OK':

		for entity in people_response['entities']:
			if entity['type'] == 'Person':

				if entity.get('quotations'):
					name=entity['text'].encode('utf-8', 'ignore')				
					name_quotation[name]=entity['quotations'][0]['quotation'].encode('utf-8', 'ignore')
	else:
		print ('Error in entity extraction call: ', people_response['statusInfo'])

	response = alchemyapi.relations('url',theUrl, {'requireEntities':1,'entities':1})

	if response['status'] == 'OK':

		for relation in response['relations']:

			relation_entity_dict={}

			if 'subject' in relation:

				if (relation['subject'].get('entities')):	
					# print('## Subject entity ##')
					for entity in relation['subject']['entities']:

						# do not deal with multiple useful entities				
						if entity['type'] == 'Person' or entity['type'] == 'Company'or entity['type'] == 'JobTitle':
							relation_entity_dict[entity['type']]=entity['text'].encode('utf-8')

			if (relation_entity_dict.has_key('Person') and len(relation_entity_dict)>0):
				personDic={}
				name_key= relation_entity_dict['Person'].encode('utf-8')	

				if (name_key not in person_list_dict.keys()):


					person=name_key.encode('utf-8').replace(" ", "%20")
					personDic['linkedInLink']="https://www.linkedin.com/vsearch/p?type=people&keywords="+person	
						
												
					if (relation_entity_dict.has_key('Company')):
						personDic['company']=relation_entity_dict['Company']
						personDic['linkedInLink']=personDic['linkedInLink']+"&company="+personDic['company']
					else:
						personDic['company']="N/A"
					if (relation_entity_dict.has_key('JobTitle')):
						personDic['job_title']=relation_entity_dict['JobTitle']
						personDic['linkedInLink']=personDic['linkedInLink']+"&title="+personDic['job_title']
					else:
						personDic['job_title']="N/A"

		
					if (name_quotation.has_key(name_key)):
						personDic['quotation']=name_quotation[name_key]
						personDic['freq']=float('inf')	
					else:
						personDic['quotation']="N/A"
						personDic['freq']=1


					person_list_dict[name_key]=personDic	
				else:
					person_list_dict[name_key]['freq']=person_list_dict[name_key]['freq']+1

		# [(k,person_list_dict[k]) for k in sorted(person_list_dict.keys())] 
			
	else:
		print('Error in relation extaction call: ', response['statusInfo'])
	

	return person_list_dict




