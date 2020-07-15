# Django项目简介
1. 本项目是一个用python3和jango框架开发简单图书管理系统，实现的功能包括图书(book)、作者(author)、出版社(publisher)、书籍摘要(detail)的**增**、**删**、**查**、**改**以及**按书籍名称搜索**等功能
2. 要运行本项目，首先要配置pyhton3.0或更高版本的python开发环境，其次要安装Django框架(开发所用版本是Django3.0.6,其他版本的兼容性尚未测试)
3. 最后要对数据库进行一些简单的配置，配置文件是/bookmanager/bookmanager/settings.py文件里的DATABASES属性,有条件的可以使用mysql数据库，不行使用sqlite3的文件数据库也可以
4. 数据库迁移命令如下
   + `python3 manager.py makemigrations`
   + `python3 manager.py makemigrate`
5. 运行服务
   + 进入项目文件夹
   + 运行命令 `python3 manager.py runserver 0.0.0.0:8000`
6. 访问服务
   + 浏览器地址栏输入`127.0.0.1:8000/publisher_list/`

# 注意事项
+ 在添加数据时，要先添加出版社和作者，再添加书籍，否则添加书籍的时候可能会没有出版社和作者可选
+ 本项目主要聚焦于项目功能的实现，没有考虑执行效率，所以项目中很多代码还可以优化。所以这只是一个演示项目，实用价值不高
+ 搜索功能目前只允许搜索书籍名称
+ 所有显示的书籍名称都可以点击跳转到该书籍的简介
