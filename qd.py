#!/usr/bin/python  
#-*-coding:utf-8-*-   
import urllib  
import urllib2  
import cookielib  
import time   
  
hosturl = 'http://123.206.92.65' 
posturl = 'http://123.206.92.65/web/useraction.php?a=dologin' 
  
cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
h = urllib2.urlopen(hosturl)  
  
headers = {'User-Agent' : 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',  
           'Referer' : 'http://123.206.92.65/web/login.php'}  
postData = {
            'qq' : 'xxxx', 
            'pass' : 'xxxx',
            }  
  
postData = urllib.urlencode(postData)  
request = urllib2.Request(posturl, postData, headers)   
response = urllib2.urlopen(request)    

qd = urllib2.urlopen('http://123.206.92.65/web/action.php?a=qiandao')
results = qd.read()
nowtime = time.strftime( '%Y-%m-%d %H:%M:%S', time.localtime( time.time() ) )
print nowtime
print results
