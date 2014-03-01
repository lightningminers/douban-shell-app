__author__ = 'xiangwenwen'

import douban_client.api
import math
import traceback
import os
import sqlite3
work_path = os.getcwd() + os.path.sep
dbPath = work_path + 'db'+os.path.sep + 'doubanShellApp.db'
errorPath = work_path + 'error' + os.path.sep + 'Douban_API_ERROR.txt'

class Music_search:
    def __init__(self):
        self.musicDic = {
            'search':self.music_search,
            'show':self.music_show
        }
        self.musicShell = ('search','show')
    def handler(self,shell,client):
        shell = shell.split(' ')
        sh = shell[0]
        shellMusic = False
        for bs in self.musicShell:
            if bs == sh:
                shellMusic = True
                break
        if shellMusic:
            try:
                clientValue = shell[1]
                self.musicDic[sh](client,clientValue)
            except IndexError:
                self.error_outinput()
                print(sh + ' your commit message is empty')
        else:
            print(sh + ' is not a douban shell command see douban help')
        pass
    #查询音乐
    def music_search(self,client,val):
        print('HTTP douban data wait ....')
        val = val.split('|')
        q = val[0]
        start = val[1]
        count = val[2]
        try:
            searchDate = client.music.search(q,start=start,count=count)
            print('\n')
            for node in searchDate['musics']:
                print('music id : ' + node['id'])
                print('music name : ' + node['title'])
                for node_ch in node['author']:
                    print('music author : ' + node_ch['name'])
                print('\n')
            print('message : select id commit up rm show tags')
        except douban_client.api.error.DoubanAPIError:
            self.error_outinput()
            print('message : search book error')
        pass
    #查询音乐详细信息
    def music_show(self,client,val):
        print('HTTP douban data wait ....')
        print('\n')
        try:
            showDate = client.music.get(val)
            print('\n')
            print('music id : ' + showDate['id'])
            print('music name : ' + showDate['title'])
            for node in showDate['author']:
                print('music author : ' + node['name'])
            print('music tags : ' + showDate['alt_title'])
            infoDic = showDate['attrs']
            print('music time : ' + infoDic['pubdate'][0])
            print('music type : ' + infoDic['media'][0])
            print('music version : ' + infoDic['version'][0])
            tracks = infoDic['tracks']
            print('music tracks : ')
            for tcks in tracks:
                print(tcks)
            print('music summary : ' + showDate['summary'])
            print('\n')
        except douban_client.api.error.DoubanAPIError:
            self.error_outinput()
            print('message : show book error')
        pass
    #错误输出
    def error_outinput(self):
        error_f = open(errorPath,'a')
        traceback.print_exc(file=error_f)
        error_f.close()
        pass
    pass
doubanMusic = Music_search()
def musicStart(client):
    music_bool = True
    while music_bool:
        music_shell = input('enter the your music shell : ')
        if music_shell == 'exit':
            music_bool = False
        else:
            doubanMusic.handler(music_shell,client)