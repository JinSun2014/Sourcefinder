#! /usr/bin/env python2.7.6
# -*- coding: utf-8 -*-

import urllib
import urllib2
import xml.etree.ElementTree as ET

def GoogleNews(subject):
    result = []
    # data = {}
    title=[]
    # data['q'] = subject
    # data['output'] = 'rss'
    #url_data = urllib.urlencode(data)
    url = r"http://news.google.com/news?" + urllib.urlencode({'q': subject, 'output': 'rss'})
    response = urllib2.urlopen(url)
    XMLTree = response.read()
    root = ET.fromstring(XMLTree)
    for r in root[0].findall('item'):
        lastIndex=r[0].text.rfind('-')
        original_source='N/A'
        unique_title=r[0].text
        if (lastIndex>-1):
            original_source=r[0].text[lastIndex+1:]
            # Reomve duplicate articles based on titles
            unique_title=r[0].text[0:lastIndex-1]
        if unique_title not in title:
            title.append(r[0].text)

            link = r[1].text
            linkset = link.split(r'http://')
            url = r'http://' + linkset[-1]
            result.append({'title': unique_title, 'url': url, 'original_source':original_source})

            # title.append(r[0].text)
            # link = r[1].text
            # linkset = link.split(r'http://')
            # url = r'http://' + linkset[-1]
            # result.append({'title': r[0].text, 'url': url})

    return result
#test case    
# print GoogleNews('China')
