__author__ = 'xiangwenwen'
import douban_client.api
class ShowUser:
    def __init__(self):
       self.showDic = {
            'search':self.search,
            'show':self.u_show
       }
       self.showShell = ('search','show')
    def handler(self,shell,client):
        shell = shell.split(' ')
        sh = shell[0]
        shellShow = False
        for bs in self.showShell:
            if bs == sh:
                shellShow = True
                break
        if shellShow:
            try:
                clientValue = shell[1]
                self.showDic[sh](client,clientValue)
            except IndexError:
                print(sh + ' your commit message is empty')
        else:
            print(sh + ' is not a douban shell command see douban help')
    def search(self,client,val):
        print('\n')
        print('HTTP douban data wait ....')
        showData = client.user.search(val)
        users = showData['users']
        try:
            for node in users:
                print('douban Id : ' + node['id'])
                print('douban Name : ' + node['name'])
            print('\n')
        except UnicodeEncodeError:
            print('douban byte error')
    def u_show(self,client,val):
        print('\n')
        print('HTTP douban data wait ....')
        try:
            u_show_Data = client.user.get(val)
            print('douban name : ' + u_show_Data['name'])
            print('douban loc :' + u_show_Data['loc_name'])
            print('douban home : ' + u_show_Data['alt'])
            print('douban registration time' + u_show_Data['created'])
            print('douban signature : ' + u_show_Data['signature'])
            print('douban id : ' + u_show_Data['id'])
            print('douban uid : ' + u_show_Data['uid'])
            print('douban loc id : ' + u_show_Data['loc_id'])
            desc = u_show_Data['desc']
            desc = desc.replace('\n','')
            le = len(desc)//2
            print('douban desc : ')
            print('    ' + desc[:le])
            print('    ' + desc[le:])
            print('\n')
        except douban_client.api.error.DoubanAPIError:
            print('douban HTTP error')
        except UnicodeEncodeError:
            print('douban byte error')
        pass
show = ShowUser()
def showme(client):
    print('HTTP douban data wait ....')
    me = client.user.me
    print('Name : ' + me['name'])
    print('Location : ' + me['loc_name'])
    pass
def showStatr(client):
 show_bool = True
 while show_bool:
    show_shell = input('enter the your user shell : ')
    if show_shell == 'exit':
        show_bool = False
    else:
        show.handler(show_shell,client)