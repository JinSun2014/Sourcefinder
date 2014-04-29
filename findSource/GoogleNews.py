#! /usr/bin/env python2.7.6

import urllib2
import xml.etree.ElementTree as ET

def GoogleNews(subject):
    result = []
    url = r"http://news.google.com/news?q=" + subject + r"&output=rss"
    response = urllib2.urlopen(url)
    XMLTree = response.read()
    root = ET.fromstring(XMLTree)
    for r in root[0].findall('item'):
        link = r[1].text
        linkset = link.split(r'http://')
        url = r'http://' + linkset[-1]
        result.append({'title': r[0].text, 'url': url})

    return result
