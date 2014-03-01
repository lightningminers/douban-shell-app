__author__ = 'xiangwenwen'
import douban_client.api
import math
import traceback
import os
import sqlite3
work_path = os.getcwd() + os.path.sep
dbPath = work_path + 'db'+os.path.sep + 'doubanShellApp.db'
errorPath = work_path + 'error' + os.path.sep + 'Douban_API_ERROR.txt'
class Book_search:
    def __init__(self):
      self.bookDic = {
          'search':self.book_search,
          'commit':self.book_commit,
          'up':self.book_update,
          'rm':self.book_remove,
          'show':self.book_show,
          'tags':self.book_tags,
          'review':self.book_reviews_show
      }
      self.bookShell = ('search','rm','up','commit','show','tags','review')
    def handler(self,shell,client):
        shell = shell.split(' ')
        sh = shell[0]
        shellBool = False
        for bs in self.bookShell:
            if bs == sh:
                shellBool = True
                break
        if shellBool:
            try:
                clientValue = shell[1]
                self.bookDic[sh](client,clientValue)
            except IndexError:
                self.error_outinput()
                print(sh + ' your commit message is empty')
        else:
            print(sh + ' is not a douban shell command see douban help')
    #搜索书籍
    def book_search(self,client,val):
       print('HTTP douban data wait ....')
       val = val.split('|')
       q = val[0]
       start = val[1]
       count = val[2]
       try:
            searchDate = client.book.search(q,start=start,count=count)
            print('\n')
            for node in searchDate['books']:
                print('book id : ' + node['id'])
                print('book name : ' + node['title'])
                print('book author : ' + node['author'][0])
                print('book publisher : ' + node['publisher'])
                print('book time : ' + node['pubdate'])
                print('\n')
            print('message : select id commit up rm show tags')
       except douban_client.api.error.DoubanAPIError:
            self.error_outinput()
            print('message : search book error')
       pass
    #给书籍评论
    def book_commit(self,client,val):
      print('HTTP douban data wait ....')
      val = val.split('|')
      bookid = val[0]
      booktitle = val[1]
      bookcontent = val[2]
      try:
            reviewsDate = client.book.review.new(bookid,booktitle,bookcontent)
            reviewsid =  reviewsDate['id']
            CX = sqlite3.connect(dbPath)
            CU= CX.cursor()
            CU.execute('insert into bookreview values (reviewid,bookid)',(reviewsid,bookid))
            CX.close()
      except douban_client.api.error.DoubanAPIError:
            self.error_outinput()
            print('message : commit book error need 150 ')
    #查看某本书籍的详细信息
    def book_show(self,client,val):
        print('HTTP douban data wait ....')
        print('\n')
        try:
            showDate = client.book.get(val)
            print('book name : ' + showDate['title'])
            print('book press : ' + showDate['publisher'])
            print('book author : ' + showDate['author'][0])
            print('book ISBN : ' + showDate['isbn13'])
            print('book time : ' + showDate['pubdate'])
            print('book price : '+ showDate['price'] + '￥')
            print('book page : '+ showDate['pages'])
            print('book douban URL : ' + showDate['alt'])
            intro = showDate['author_intro']
            intro = intro.replace('\n','')
            intro_num = len(intro) // 2
            print('book author intro : ' + intro)
            # summary = showDate['summary']
            # summary = summary.replace('\n','')
            # print('book summary : ' + summary)
            print('\n')
        except douban_client.api.error.DoubanAPIError:
            self.error_outinput()
            print('message : show book error')
    #更新书籍的某条评论
    def book_update(self,client,val):
        print('HTTP douban update reviews wait ....')
        val = val.split('|')
        reviewsid = val[0]
        newtitle = val[1]
        newcontent = val[2]
        try:
            client.book.review.update(reviewsid,newtitle,newcontent)
            print('message : update success')
        except douban_client.api.error.DoubanAPIError:
            self.error_outinput()
            print('message : HTTP error')
    #删除书籍的某条评论
    def book_remove(self,client,val):
        print('HTTP douban remove reviews wait ....')
        try:
            client.book.review.delete(val)
            print('message : remove reviews success')
        except douban_client.api.error.DoubanAPIError:
            self.error_outinput()
            print('message : HTTP error')
    #查看书籍的标签
    def book_tags(self,client,val):
       try:
          tagsData = client.book.tags(val)
          tags = tagsData['tags']
          print('\n')
          for node in tags:
               print('tag : ' + node['title'])
          print('\n')
       except douban_client.api.error.DoubanAPIError:
          self.error_outinput()
          print('value error or HTTP error')
    #查看评论书籍之后的reviews id
    def book_reviews_show(self,val):
        bookid = val
        CX = sqlite3.connect(dbPath)
        CU= CX.cursor()
        CU.execute('select * from bookreview where bookid="%s"'%bookid)
        reviewID = CU.fetchall()
        print('view bookid as reviewsid' + bookid)
        print(reviewID)
        CX.close()
    #错误信息输出
    def error_outinput(self):
        error_f = open(errorPath,'a')
        traceback.print_exc(file=error_f)
        error_f.close()
        pass
doubanBook = Book_search()
def bookStart(client):
  book_bool = True
  while book_bool:
      book_shell = input('enter the your book shell : ')
      if book_shell == 'exit':
          book_bool = False
      else:
          doubanBook.handler(book_shell,client)