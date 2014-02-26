__author__ = 'xiangwenwen'
import douban_user
import douban_help
import douban_book
def  center():
    shell = input('enter the your master shell : ')
    return shell
    pass
shellDic = {
    'show me':douban_user.showme,
    'user':douban_user.userStatr,
    'douban help':douban_help.dbhelp,
    'book':douban_book.bookStatr
}

