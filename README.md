## zk-spider
-----
###关于此项目的想法

####首先谈谈需求

保存页面并按时间分隔保存在设定的目录下，保存目录可能会涉及到\和/的转换以及地址的拼接

保存图片，css和js的想法是按照经验css会在head里外联，js会在body的尾端以用来优化加载速度，图片的话现在大致想法是获得所有img标签的href值

为了使打开效果一致，在下载完css，js和图片以后应该更改网页中引用它们的本地地址来确定服务器中的更改对本地无效

-----

####一些工具选择

以前没做过命令行加参数的东西，遂百度get argparse一枚，去官方文档看了下例子，决定直接用argparse了

爬虫一类还是用最常用的requests+beautifulsoup4了（requests记得关闭keep-alive）


-----
####Some Note

根据前几天看Fluent Python的经验，获取文件名可以这样

    import os  
    _, name = os.path.split(file)

在进行第一次测试的时候发现，不加User-Agent访问的是彩版网站，遂添加了chrome的UA

然后爬取下来发现是一个跳转代码，在chrome的开发者工具查看网络发现发生了302跳转，于是抓取分为两次，第一次获得跳转的地址，第二次获得网页

------

目前问题：网页随机跳转。。。和网页中链接地址更改（此处可以做出来但是我想把代码精简一下）

网页跳转

![](http://7qnaxb.com1.z0.glb.clouddn.com/mark1.png)

此处大概是爬下来频率最高的，先是一个302跳转，接着200返回一个可以跳转的网页，最后跳转到最终想得到的网页

![](http://7qnaxb.com1.z0.glb.clouddn.com/mark2.png)

还有这种根本不跳转的，直接原网址返回

![](http://7qnaxb.com1.z0.glb.clouddn.com/mark3.png)

这种丧病第一个返回跳转链接，然后302返回另一个链接，最后在跳转到最终网页的
