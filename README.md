# xuegod自助签到
我本地用的是centos7自带的python2.7.5
修改qd.py 的xxxx为自己的用户名和密码，放到有外网的服务器上，再设置一个crontab定时任务就ok了。
05 20 * * * python ~/qd.py >>qdrecord.log

后面更高级的玩法，可以抓取日志，匹配日期和签到成功，就发email到邮箱，或者短信提醒...
