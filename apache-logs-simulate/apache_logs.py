#!/usr/bin/python
import time
import datetime
import random
timestr = time.strftime("%Y%m%d-%H%M%S")

f = open('access_log_'+timestr+'.log','w')

ips=["89.163.241.243","89.163.241.217","89.163.241.246","89.163.241.242","89.163.241.230","89.163.241.248","89.163.241.231","89.163.241.218","89.163.241.245","89.163.241.244","89.163.241.250","189.113.171.3","200.170.82.192","69.163.253.137","155.94.64.210","177.10.165.112","177.11.52.236","177.154.148.17","177.185.200.107","177.185.200.108","177.185.200.120","177.185.200.128","177.185.200.137","189.113.166.100","192.175.106.222","200.147.33.61","200.183.174.2","200.98.199.12","200.98.199.13","201.82.1.24","201.87.225.53","201.87.225.61","209.133.214.29","209.239.112.110","23.239.85.194","74.52.129.242","89.163.241.234","89.163.241.235","89.163.241.215","89.163.241.232","89.163.241.241","89.163.241.247","89.163.241.240","89.163.241.249","89.163.241.251","200.180.14.194","191.189.220.77","177.193.71.222","186.225.240.148","186.209.255.235","187.55.39.36","187.102.39.63","200.208.9.237","152.238.239.169","131.72.128.248","179.218.247.199","201.76.210.2","170.231.225.131","191.32.240.251","170.231.224.195","170.231.225.15","189.106.73.177","200.189.9.38","186.224.43.212","189.89.213.215","170.231.226.252","187.85.239.106","189.89.220.161","189.89.221.69","168.121.90.245","168.194.152.56","177.185.103.215","186.195.135.208","187.84.245.60","186.216.137.215","186.236.229.250","177.39.125.158","177.91.119.193","186.244.66.127","191.253.71.48","177.75.109.38","179.189.22.174","191.177.201.252","187.17.229.26","186.209.182.84","187.87.2.96","138.36.142.186","168.181.198.22","177.54.105.231","152.254.194.77","177.81.47.145","177.81.207.60","189.68.57.9","200.185.202.157","187.4.35.180","187.54.205.158","187.107.52.207","189.27.174.211","177.18.160.129","177.73.2.204","177.20.248.15","177.190.117.188","177.4.209.244","187.109.230.167","170.150.78.219","168.227.41.166","189.70.130.246","170.78.97.183","177.6.72.27","179.187.255.115","201.34.239.18","179.255.143.94","168.227.30.200","201.11.191.66","177.38.248.55","138.36.63.27","177.132.244.0","187.28.123.81","168.90.0.9","168.90.3.32","177.16.233.186","177.134.176.94","187.1.124.53","152.238.45.212","187.41.12.178","189.115.96.142","200.180.14.194","200.208.9.237","123.221.14.56","16.180.70.237","10.182.189.79","218.193.16.244","198.122.118.164","114.214.178.92","233.192.62.103","244.157.45.12","81.73.150.239","237.43.24.118","168.181.198.22","177.75.109.38","187.85.239.106","138.122.141.73","187.87.2.96","24.28.2.247","24.89.58.78","24.158.246.23","147.0.234.148","72.255.22.124","167.61.108.240","186.52.224.3","24.89.58.78","24.158.246.23","147.0.234.148","72.255.22.124","167.61.108.240","186.52.224.3","167.61.10.94","167.58.47.19","186.52.65.128","109.204.46.230","92.25.163.168","82.153.105.63","83.67.176.115","92.7.52.21","82.218.220.75","82.218.220.221","185.61.171.192","31.185.98.152","89.190.116.97","84.46.175.193","24.138.174.42","205.250.193.154","69.60.71.44","84.238.58.103","186.107.207.191"]
referers=["-","http://www.casualcyclist.com","http://bestcyclingreviews.com/top_online_shops","http://bleater.com","http://searchengine.com"]
resources=["/handle-bars","/stems","/wheelsets","/forks","/seatposts","/saddles","/shifters","/Store/cart.jsp?productID="]
useragents=["Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36","Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25","Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201","Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0","Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))"]

otime = datetime.datetime(2013,10,10)

for i in xrange(0,5000):
	increment = datetime.timedelta(seconds=random.randint(30,300))
	otime += increment
	uri = random.choice(resources)
	if uri.find("Store")>0:
		uri += `random.randint(10000,15000)`
	ip = random.choice(ips)
	useragent = random.choice(useragents)
	referer = random.choice(referers)
        f.write('{"clientip": "%s", "teste1": "- -", "teste3": "[%s]",  "teste3": "GET %s HTTP/1.0", "teste4": "200 %s", "teste5": "%s", "teste6": "%s"}\n' % (random.choice(ips),otime.strftime('%d/%b/%Y:%H:%M:%S %z'),uri,random.randint(20000,50000),referer,useragent))
