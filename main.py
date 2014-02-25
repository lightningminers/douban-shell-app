__author__ = 'xiangwenwen'

import sys
import subprocess
import urllib.request
import os
import douban_client.api
import OAuth
sys.path.append('src')
import douban_controlCenter
client = OAuth.addOAuth()
if client == 'error':
    print('error oauth')
else:
    while True:
           shell = douban_controlCenter.center()
           if shell == 'exit':
                exit()
                pass
           try:
               douban_controlCenter.shellDic[shell](client)
               pass
           except KeyError:
                print(shell +  ' is not a douban shell command see douban help')
                continue      
           except  KeyboardInterrupt:
                exit()     
    pass