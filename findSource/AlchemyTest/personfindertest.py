#!/usr/bin/python


import sys

from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

#for json call only
import json

def GetPeople(url):
	people = []
	people_response = alchemyapi.entities("url", url, { 'requireEntities':1,'entities':1,'quotations':1 })
	if people_response['status'] == 'OK':

		for entity in people_response['entities']:
			if entity['type'] == 'Person':
				#print "====="
				#print entity['text']
				people.append(entity['text'])
				#people.append(entity)

	return people

#print GetPeople('http://www.cnn.com/2014/06/02/us/bowe-bergdahl-questions/')

