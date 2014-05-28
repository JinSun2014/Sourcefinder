#!/usr/bin/python

from alchemytest import GetPeople
import time
import threading

threadstart = time.clock()
threadclock = time.time()

def worker(num, url):
	print "===Article " + str(num) + "===\n" + str(GetPeople(url))
	#print GetPeople(url)
	return

# urls = ['http://www.theverge.com/2014/5/26/5753026/google-and-nest-considering-home-security',
# 		'http://www.foxbusiness.com/technology/2014/05/27/report-google-nest-plotting-home-security-push-potential-dropcam-buy/',
# 		'http://venturebeat.com/2014/05/27/google-considers-a-home-security-move-through-nest-eyes-dropcam/',
# 		'http://gizmodo.com/report-google-and-nest-want-to-offer-home-surveillance-1581923666',
# 		'http://www.forbes.com/sites/michaelwolf/2014/05/27/googles-biggest-problem-as-home-security-provider-consumer-trust/',
# 		'http://gantdaily.com/2014/05/27/nest-labs-recalls-to-repair-nest-protect-smoke-co-alarms-due-to-failure-to-sound-alert/',
# 		'http://www.zacks.com/stock/news/134823/google-to-relaunch-nest-protect',
# 		'http://mindofthegeek.com/2014/05/27/google-may-acquire-dropcam-through-nest/',
# 		'http://invezz.com/news/equities/11187-google-share-price-nest-mulls-dropcam-acquisition']
# threads = []

# t1 = threading.Thread(target=worker, args=(1,urls[1],))
# t2 = threading.Thread(target=worker, args=(2,urls[2],))
# t3 = threading.Thread(target=worker, args=(3,urls[3],))
# t4 = threading.Thread(target=worker, args=(4,urls[4],))
# t5 = threading.Thread(target=worker, args=(5,urls[5],))
# t6 = threading.Thread(target=worker, args=(6,urls[6],))
# t7 = threading.Thread(target=worker, args=(7,urls[7],))
# t8 = threading.Thread(target=worker, args=(8,urls[8],))
# t9 =  threading.Thread(target=worker, args=(9,urls[0],))

t1 = threading.Thread(target=worker, args=(1,'http://www.theverge.com/2014/5/26/5753026/google-and-nest-considering-home-security',))
t2 = threading.Thread(target=worker, args=(2,'http://www.foxbusiness.com/technology/2014/05/27/report-google-nest-plotting-home-security-push-potential-dropcam-buy/',))
t3 = threading.Thread(target=worker, args=(3,'http://venturebeat.com/2014/05/27/google-considers-a-home-security-move-through-nest-eyes-dropcam/',))
t4 = threading.Thread(target=worker, args=(4,'http://gizmodo.com/report-google-and-nest-want-to-offer-home-surveillance-1581923666',))
t5 = threading.Thread(target=worker, args=(5,'http://www.forbes.com/sites/michaelwolf/2014/05/27/googles-biggest-problem-as-home-security-provider-consumer-trust/',))
t6 = threading.Thread(target=worker, args=(6,'http://gantdaily.com/2014/05/27/nest-labs-recalls-to-repair-nest-protect-smoke-co-alarms-due-to-failure-to-sound-alert/',))
t7 = threading.Thread(target=worker, args=(7,'http://www.zacks.com/stock/news/134823/google-to-relaunch-nest-protect',))
t8 = threading.Thread(target=worker, args=(8,'http://mindofthegeek.com/2014/05/27/google-may-acquire-dropcam-through-nest/',))
t9 =  threading.Thread(target=worker, args=(9,'http://invezz.com/news/equities/11187-google-share-price-nest-mulls-dropcam-acquisition',))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()


threadend = time.clock()
threadclockend = time.time()
print "===Full Time: " + str(threadend - threadstart) + "==="
print "===CLOCK TIME: " + str(threadclockend - threadclock) + "==="

clockstart = time.time()
fullstart = time.clock()

print "First Article"
start = time.clock()
print GetPeople('http://www.theverge.com/2014/5/26/5753026/google-and-nest-considering-home-security')
end = time.clock()
print "Article 1 Time: " + str(end - start)

print "===Second Article==="
print GetPeople('http://www.foxbusiness.com/technology/2014/05/27/report-google-nest-plotting-home-security-push-potential-dropcam-buy/')
print "===Third Article==="
print GetPeople('http://venturebeat.com/2014/05/27/google-considers-a-home-security-move-through-nest-eyes-dropcam/')
print "===Fourth Article==="
print GetPeople('http://gizmodo.com/report-google-and-nest-want-to-offer-home-surveillance-1581923666')
print "===Fifth Article==="
print GetPeople('http://www.forbes.com/sites/michaelwolf/2014/05/27/googles-biggest-problem-as-home-security-provider-consumer-trust/')
print "===Sixth Article==="
print GetPeople('http://gantdaily.com/2014/05/27/nest-labs-recalls-to-repair-nest-protect-smoke-co-alarms-due-to-failure-to-sound-alert/')
print "===Seventh Article==="
print GetPeople('http://www.zacks.com/stock/news/134823/google-to-relaunch-nest-protect')
print("===Eigth Article===")
print GetPeople('http://mindofthegeek.com/2014/05/27/google-may-acquire-dropcam-through-nest/')
print("===Ninth Article===")
print GetPeople('http://invezz.com/news/equities/11187-google-share-price-nest-mulls-dropcam-acquisition')


fullend = time.clock()
clockend = time.time()
print "===Full Time: " + str(fullend - fullstart) + "==="
print "===CLOCK TIME: " + str(clockend - clockstart) + "==="