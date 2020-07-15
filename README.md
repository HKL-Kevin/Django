# Django项目简介
+ 1. 本项目是一个用python3和jango框架开发简单图书管理系统，实现的功能包括图书(book)、作者(author)、出版社(publisher)、书籍摘要(detail)的增、删、查、改以及书籍搜索等功能
+ 2. 要运行本项目，首先要配置pyhton3.0或更高版本的python开发环境，其次要安装Django框架(开发所用版本是Django3.0.6,其他版本的兼容性尚未测试)
+ 3. 最后要对数据库进行一些简单的配置，配置文件是/bookmanager/bookmanager/settings.py文件里的DATABASES属性,有条件的可以使用mysql数据库，不行使用sqlite3的文件数据库也可以
+ 4. 数据库迁移命令如下
      + `python3 manager.py makemigrations`
      + `python3 manager.py makemigrate`
