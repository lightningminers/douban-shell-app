__author__ = 'xiangwenwen'
import douban_client.api
import math
import os
import sqlite3
dbPath = os.getcwd() + os.path.sep+'db'+os.path.sep + 'doubanShellApp.db'
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
                print(sh + ' your commit message is empty')
        else:
            print(sh + ' is not a douban shell command see douban help')
    def book_search(self,client,val):
       print('HTTP douban data wait ....')
       val = val.split('|')
       q = val[0]
       start = val[1]
       count = val[2]
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
       pass
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
          print(douban_client.api.error.DoubanAPIError)
          print('need more than 150 words')
    def book_show(self,client,val):
        try:
            print('HTTP douban data wait ....')
            print('\n')
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
            print(douban_client.api.error.DoubanAPIError)
            print('book not found')
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
            print('message : HTTP error')
    def book_remove(self,client,val):
        print('HTTP douban remove reviews wait ....')
        try:
            client.book.review.delete(val)
            print('message : remove reviews success')
        except douban_client.api.error.DoubanAPIError:
            print('message : HTTP error')
    def book_tags(self,client,val):
       try:
          tagsData = client.book.tags(val)
          tags = tagsData['tags']
          print('\n')
          for node in tags:
               print('tag : ' + node['title'])
          print('\n')
       except douban_client.api.error.DoubanAPIError:
          print(douban_client.api.error.DoubanAPIError)
          print('value error or HTTP error')
    def book_reviews_show(self,val):
        bookid = val
        CX = sqlite3.connect(dbPath)
        CU= CX.cursor()
        CU.execute('select * from bookreview where bookid="%s"'%bookid)
        reviewID = CU.fetchall()
        print('view bookid as reviewsid' + bookid)
        print(reviewID)
        CX.close()
book = Book_search()
def bookStatr(client):
  book_bool = True
  while book_bool:
      book_shell = input('enter the your book shell : ')
      if book_shell == 'exit':
          book_bool = False
      else:
          book.handler(book_shell,client)