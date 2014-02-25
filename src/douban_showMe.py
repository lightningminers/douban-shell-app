__author__ = 'xiangwenwen'

def showme(client):
    me = client.user.me
    print('Name : ' + me['name'])
    print('Location : ' + me['loc_name'])
    pass