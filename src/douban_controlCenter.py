__author__ = 'xiangwenwen'
import douban_showMe
import douban_help
import douban_book
def  center():
    shell = input('enter the your master shell : ')
    return shell
    pass
shellDic = {
    'show me':douban_showMe.showme,
    'douban help':douban_help.dbhelp,
    'book':douban_book.bookStatr
}

