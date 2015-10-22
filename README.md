# zk-spider
-----
###关于此项目的想法

####首先谈谈需求

保存页面并按时间分隔保存在设定的目录下，保存目录可能会涉及到\和/的转换以及地址的拼接

保存图片，css和js的想法是按照经验css会在head里外联，js会在body的尾端以用来优化加载速度，图片的话现在大致想法是获得所有img标签的href值

为了使打开效果一致，在下载完css，js和图片以后应该更改网页中引用它们的本地地址来确定服务器中的更改对本地无效

-----

一些工具选择

以前没做过命令行加参数的东西，遂百度get argparse一枚，去官方文档看了下例子，决定直接用argparse了

爬虫一类还是用最常用的requests+beautifulsoup4了（requests记得关闭keep-alive）


-----
Some Note

根据前几天看Fluent Python的经验，获取文件名可以这样


    import os  
    _, name = os.path.split(file)
