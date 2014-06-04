#!/usr/bin/python

from alchemytest import GetPeople
#from personfindertest import GetPeople
from GoogleNews import GoogleNews
from YahooFinance import YahooFinance


import time
import threading


threadstart = time.clock()
threadclock = time.time()

def worker(num, url, result):
	#print "===Article " + str(num) + "===\n" + str(GetPeople(url))
	#print "run"
	#print readArticle(url, 'Some News Source')
	#print GetPeople(url)
	#print GetPeople(url)

	result.append(GetPeople(url))
	return

#OLD OLD TESTS

# urls = ['http://www.theverge.com/2014/5/26/5753026/google-and-nest-considering-home-security',
# 		'http://www.foxbusiness.com/technology/2014/05/27/report-google-nest-plotting-home-security-push-potential-dropcam-buy/',
# 		'http://venturebeat.com/2014/05/27/google-considers-a-home-security-move-through-nest-eyes-dropcam/',
# 		'http://gizmodo.com/report-google-and-nest-want-to-offer-home-surveillance-1581923666',
# 		'http://www.forbes.com/sites/michaelwolf/2014/05/27/googles-biggest-problem-as-home-security-provider-consumer-trust/',
# 		'http://gantdaily.com/2014/05/27/nest-labs-recalls-to-repair-nest-protect-smoke-co-alarms-due-to-failure-to-sound-alert/',
# 		'http://www.zacks.com/stock/news/134823/google-to-relaunch-nest-protect',
# 		'http://mindofthegeek.com/2014/05/27/google-may-acquire-dropcam-through-nest/',
# 		'http://invezz.com/news/equities/11187-google-share-price-nest-mulls-dropcam-acquisition']

#list = [];
def getSources(topic):
	#urls = ['http://www.postcrescent.com/article/20140517/APC03/305170255/Integrys-Energy-growing-shareholders-told', 
	#		'http://www.postcrescent.com/article/20140517/APC03/305170255/Integrys-Energy-growing-shareholders-told']
	urls = GoogleNews(topic)
	urls.extend(YahooFinance(topic))
	print urls

	print len(urls)


	#NEWER CODE
	numUrls = len(urls)
	threads = []
	names = []


	for i in range(0, numUrls):
		t= threading.Thread(target=worker, args=(i,urls[i],names))
		threads.append(t)
		t.start()

	for p in threads:
	     p.join()

	return names

# threadend = time.clock()
# threadclockend = time.time()

# for item in names:
#  	print item

# print "===Full Time: " + str(threadend - threadstart) + "==="
# print "===CLOCK TIME: " + str(threadclockend - threadclock) + "==="

#print getSources('test')





# clockstart = time.time()
# fullstart = time.clock()

# for i in range(0, numUrls-1):
# 	print "===Article " + str(i) + "===\n" + str(GetPeople(urls[i]))



# fullend = time.clock()
# clockend = time.time()
# print "===Full Time: " + str(fullend - fullstart) + "==="
# print "===CLOCK TIME: " + str(clockend - clockstart) + "==="
