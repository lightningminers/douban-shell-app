##what##

此项目，是基于douban-client python SDK项目开发的douban shell版，一切都回归到命令行时代，在终端中登陆，查看信息等。

##如何使用##

在OAuth.py文件中，找到API_KEY，API_SECRET，配置上在豆瓣申请的key，CALLBACK_URL填写上在豆瓣应用申请界面中填写的回调URL

在回调URL中，最主要的是拿到授权成功之后的code。

##开发日志信息##

> 2014年2月23日			实现了oauth2.0认证
>
> 2014年2月24日中午        基础构造搭建，show me，book shell  douban help命令
>
> 2014年2月24日 夜 10：00 		完成book enter 中show search commit 命令
>
> 2014年2月25日 中午       完成了show-search-show命令，book-show命令，book-tags命令