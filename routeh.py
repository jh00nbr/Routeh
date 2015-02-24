#!/usr/bin/env python
# -*- coding: utf-8 -*-

#                  _       _   
#      ___ ___ _ _| |_ ___| |_ 
#     |  _| . | | |  _| -_|   |
#     |_| |___|___|_| |___|_|_|
#
# Autor: Jhonathan Davi | Jhoon b4kunin_m4l
# Facebook: www.facebook.com/JhonVipNet
# Page: www.facebook.com/InurlBrasil
# Blog: http://blog.inurl.com.br
# Twitter: twitter.com/jh00nbr
# Youtube: www.youtube.com/user/Mrsinisterboy
 
from shodan import WebAPI
import requests
url = requests.get('http://127.0.0.1/get.php')
 

 
 
print url.status_code

if url.status_code == 200:
	print 'Status is:', url.status_code 
	





