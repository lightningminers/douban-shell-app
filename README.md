##what##

此项目，是基于douban-client python SDK项目开发的douban shell版，一切都回归到命令行时代。

##已经支持的功能##

>支持oauth2.0认证
>
>支持查看登陆用户信息
>
>支持查询用户，查看查询用户的详细信息，关注用户，取消关注用户
>
>支持查询书籍，查看查询书籍的详细信息，书籍评论，更新书籍评论，删除书籍评论，查看书籍标签，查看review id。

##如何使用##

在config.py文件中，找到API_KEY，API_SECRET，配置上在豆瓣申请的key，CALLBACK_URL填写上在豆瓣应用申请界面中填写的回调URL

，SCOPE填写上在豆瓣应用中申请的权限，在回调URL中，最主要的是拿到授权成功之后的code。

##开发日志信息##

> 2014年2月23日			实现了oauth2.0认证
>
> 2014年2月24日中午        基础构造搭建，show me，book shell  douban help命令
>
> 2014年2月24日 夜 10：00 		完成book enter 中show search commit 命令
>
> 2014年2月25日 中午       完成了show-search-show命令，book-show命令，book-tags命令
>
> 2014年2月25日 夜 10：00 		初始化时创建SQLITE数据库，完成book-rm命令，完成book-up命令，完成book-review命令
>
> 2014年2月26日  晨        移除show顶级命令，增加user命令，完成user-search，user-show，user-follow，user-unfollow命令