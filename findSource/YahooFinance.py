#! /usr/bin/env python2.7.3

import json
import urllib, urllib2
import xml.etree.ElementTree as ET

def getSymbol(subject):
    url = r'http://d.yimg.com/autoc.finance.yahoo.com/autoc?'\
        + urllib.urlencode({'query': subject, 'callback': 'YAHOO.Finance.SymbolSuggest.ssCallback'})
    response = urllib2.urlopen(url)
    res = response.read()
    j = res[res.find('(') + 1 : -1]
    data = json.loads(j)
    symbol = None
    try:
        symbol = data['ResultSet']['Result'][0]['symbol']
    except Exception as e:
        symbol = None

    return symbol

def YahooFinance(subject):
    symbol = getSymbol(subject)
    if symbol is None:
        return []

    url = r'http://finance.yahoo.com/rss/headline?'\
        + urllib.urlencode({'s':symbol})
    response = urllib2.urlopen(url)
    XMLTree = response.read()
    root = ET.fromstring(XMLTree)
    result = []
    titlelist = []

    for r in root[0].findall('item'):
        title = r[0].text.encode('utf8')
        if 'video' not in title and 'audio' not in title\
            and '$$' not in title and title not in titlelist:
            link = r'http://' + r[1].text.split(r'http://')[-1]
            result.append({'title': title, 'url': link})
            titlelist.append(title)

    return result

if __name__ == "__main__":
    #print YahooFinance('yapei')
    print YahooFinance('comcast')
    #print YahooFinance('comcast corporation')
