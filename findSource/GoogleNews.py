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
        # Reomve duplicate articles based on titles
        if r[0].text not in title:
            title.append(r[0].text)

            link = r[1].text
            linkset = link.split(r'http://')
            url = r'http://' + linkset[-1]
            result.append({'title': r[0].text, 'url': url})

            # title.append(r[0].text)
            # link = r[1].text
            # linkset = link.split(r'http://')
            # url = r'http://' + linkset[-1]
            # result.append({'title': r[0].text, 'url': url})

    return result
#test case    
# print GoogleNews('China')
