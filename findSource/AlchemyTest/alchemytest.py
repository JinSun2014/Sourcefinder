import sys

from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

#for json call only
import json

def readArticle(myUrl):

    #return list
    output = {}

    response = alchemyapi.title("url", myUrl)
    output['title'] = response['title'].encode('utf-8', 'ignore')
    if output['title'] =='':
    	output['title']='No title found'


    response = alchemyapi.author("url", myUrl)

    output['author'] = response["author"].encode('utf-8', 'ignore')
    if output['author'] =='':
    	output['author'] = 'anonym'

    #response = alchemyapi.entities("url", myUrl, { 'quotations':1 })

    #print(json.dumps(response, indent=4))

    output['people'] = GetPeople(myUrl)
    output['url'] = myUrl
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

			if (relation_entity_dict.has_key('Person') and len(relation_entity_dict)>1):
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

		[(k,person_list_dict[k]) for k in sorted(person_list_dict.keys())] 
		
			
	else:
		print('Error in relation extaction call: ', response['statusInfo'])
	# person_list = []

	# people_response = alchemyapi.entities("url", theUrl, { 'quotations':1 })

	# name_quotation={}
	# if people_response['status'] == 'OK':

	# 	for entity in people_response['entities']:
	# 		if entity['type'] == 'Person':

	# 			if entity.get('quotations'):
	# 				name=entity['text'].encode('utf-8', 'ignore')				
	# 				name_quotation[name]=entity['quotations'][0]['quotation'].encode('utf-8', 'ignore')
	# else:
	# 	print ('Error in entity extraction call: ', people_response['statusInfo'])

	# previous_namelist=[]
	# response = alchemyapi.relations('url',theUrl, {'requireEntities':1,'entities':1})

	# if response['status'] == 'OK':

	# 	for relation in response['relations']:

	# 		# relation_entity_list=[]
	# 		relation_entity_dict={}

	# 		if 'subject' in relation:

	# 			if (relation['subject'].get('entities')):	
	# 				# print('## Subject entity ##')
	# 				for entity in relation['subject']['entities']:

	# 					# do not deal with multiple useful entities				
	# 					if entity['type'] == 'Person' or entity['type'] == 'Company'or entity['type'] == 'JobTitle':
	# 						relation_entity_dict[entity['type']]=entity['text'].encode('utf-8')
	# 						# print ('Entity type:', entity['type'])
	# 						# print ('Entity text:', entity['text'].encode('utf-8'))
	# 						# relation_entity_list.append(entity)

			
	# 		if 'object' in relation:
	# 			# print('Object: ', relation['object']['text'].encode('utf-8'))
	# 			if (relation['object'].get('entities')):	
	# 				# print('## Object entity ##')
	# 				for entity in relation['object']['entities']:
					
	# 					if entity['type'] == 'Person' or entity['type'] == 'Company'or entity['type'] == 'JobTitle':
	# 						relation_entity_dict[entity['type']]=entity['text'].encode('utf-8')
	# 						# print ('Entity type:', entity['type'])
	# 						# print ('Entity text:', entity['text'].encode('utf-8'))	
	# 						# relation_entity_list.append(entity)
	# 		# print ('## relation_entity_list ##')
	# 		if len(relation_entity_dict)>1:
	# 			# for key, value in relation_entity_dict.items():
	# 			# 	print (key, value)
				
	# 			if (relation_entity_dict.has_key('Person') and len(relation_entity_dict)>1):
	# 				personDic={}
	# 				personDic['name'] = relation_entity_dict['Person'].encode('utf-8')	
	# 				if (personDic['name'] not in previous_namelist):

	# 					previous_namelist.append(personDic['name'])

	# 					person=personDic['name'].encode('utf-8').replace(" ", "%20")
	# 					personDic['linkedInLink']="https://www.linkedin.com/vsearch/p?type=people&keywords="+person	
							
													
	# 					if (relation_entity_dict.has_key('Company')):
	# 						personDic['company']=relation_entity_dict['Company']
	# 						personDic['linkedInLink']=personDic['linkedInLink']+"&company="+personDic['company']
	# 					else:
	# 						personDic['company']="N/A"
	# 					if (relation_entity_dict.has_key('JobTitle')):
	# 						personDic['job_title']=relation_entity_dict['JobTitle']
	# 						personDic['linkedInLink']=personDic['linkedInLink']+"&title="+personDic['job_title']
	# 					else:
	# 						personDic['job_title']="N/A"
	# 					personDic['twitterLink']="https://twitter.com/search?q="+person+"&src=corr&mode=users"			
	# 					personDic['FacebookLink']="https://www.facebook.com/search/more/?q="+person
			
	# 					if (name_quotation.has_key(personDic['name'])):
	# 						personDic['quotation']=name_quotation[personDic['name']]	
	# 					else:
	# 						personDic['quotation']="N/A"

	# 					# for key, value in personDic.items():
	# 					# 	print (key, value)		
	# 					# print('')
	# 					# print('')
	# 					person_list.append(personDic)

	# 		# print('## relation_entity_list ##')
	# 		# for entity in relation_entity_list:
	# 		# 	print ('Entity type:', entity['type'])
	# 		# 	print ('Entity text:', entity['text'].encode('utf-8'))	
			
	# else:
	# 	print('Error in relation extaction call: ', response['statusInfo'])

	return person_list_dict


