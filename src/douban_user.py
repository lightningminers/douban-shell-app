__author__ = 'xiangwenwen'
import douban_client.api
import os
import traceback
work_path = os.getcwd() + os.path.sep
errorPath = work_path + 'error' + os.path.sep + 'Douban_API_ERROR.txt'
class User:
    def __init__(self):
       self.userDic = {
            'search':self.search,
            'show':self.current_user_show,
            'follow':self.user_follow,
            'unfollow':self.user_unfollow
       }
       self.userShell = ('search','show','follow','unfollow')
    def handler(self,shell,client):
        shell = shell.split(' ')
        sh = shell[0]
        shellUser = False
        for bs in self.userShell:
            if bs == sh:
                shellUser = True
                break
        if shellUser:
            try:
                clientValue = shell[1]
                self.userDic[sh](client,clientValue)
            except IndexError:
                self.error_outinput()
                print(sh + ' your commit message is empty')
        else:
            print(sh + ' is not a douban shell command see douban help')
    #查询用户
    def search(self,client,val):
        print('\n')
        print('HTTP douban data wait ....')
        search_user_data = client.user.search(val)
        users = search_user_data['users']
        try:
            for node in users:
                print('douban Id : ' + node['id'])
                print('douban Name : ' + node['name'])
            print('\n')
        except UnicodeEncodeError:
            self.error_outinput()
            print('douban byte error')
        except douban_client.api.error.DoubanAPIError:
            self.error_outinput()
            print('douban HTTP error')
    #显示当前查询的一个用户的详细信息
    def current_user_show(self,client,val):
        print('\n')
        print('HTTP douban data wait ....')
        try:
            current_user_show_data = client.user.get(val)
            print('douban name : ' + current_user_show_data['name'])
            print('douban loc :' + current_user_show_data['loc_name'])
            print('douban home : ' + current_user_show_data['alt'])
            print('douban registration time' + current_user_show_data['created'])
            print('douban signature : ' + current_user_show_data['signature'])
            print('douban id : ' + current_user_show_data['id'])
            print('douban uid : ' + current_user_show_data['uid'])
            print('douban loc id : ' + current_user_show_data['loc_id'])
            desc = current_user_show_data['desc']
            desc = desc.replace('\n','')
            le = len(desc)//2
            print('douban desc : ')
            print('    ' + desc[:le])
            print('    ' + desc[le:])
            print('\n')
        except douban_client.api.error.DoubanAPIError:
            self.error_outinput()
            print('douban HTTP error')
        except UnicodeEncodeError:
            self.error_outinput()
            print('douban byte error')
        pass
    #关注用户
    def user_follow(self,client,val):
        try:
            user_follow_data = client.user.follow(val)
            if user_follow_data['following']:
                print('following success')
                print('name following : ' + user_follow_data['screen_name'])
                print('douban url : ' + user_follow_data['url'])
            else:
                print('following error')
        except douban_client.api.error.DoubanAPIError:
            self.error_outinput()
            print('douban HTTP error')
        pass
    #取消关注用户
    def user_unfollow(self,client,val):
        try:
            user_unfollow_data = client.user.unfollow(val)
            if user_unfollow_data['following']:
                print('unfollowing success')
                print('name unfollowing : ' + user_unfollow_data['screen_name'])
                print('douban url : ' + user_unfollow_data['url'])
        except douban_client.api.error.DoubanAPIError:
            self.error_outinput()
            print('douban HTTP error')
        pass
    #错误信息输出
    def error_outinput(self):
        error_f = open(errorPath,'a')
        traceback.print_exc(file=error_f)
        error_f.close()
        pass
doubanUser = User()
def showme(client):
    print('HTTP douban data wait ....')
    me = client.user.me
    print('Name : ' + me['name'])
    print('Location : ' + me['loc_name'])
    pass
def userStatr(client):
 user_bool = True
 while user_bool:
    user_shell = input('enter the your user shell : ')
    if user_shell == 'exit':
        user_bool = False
    else:
        doubanUser.handler(user_shell,client)