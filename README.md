# zhihu_follower
[toc]

## 项目简介

* 这是一个兴趣使然的小项目，可以说想学爬虫的初衷就是因为知乎一直给我送僵尸粉，我非常好奇我究竟有多少僵尸粉，多少真粉丝。于是开始学习爬虫，完成了这个爬去知乎用户粉丝信息的项目。😁
* 总是听闻知乎反爬很厉害，但是当了解了web的一些基本知识之后，还是可以通过一些方法爬取信息的，在这个项目中我会将我用的办法进行说明。🎃
* 本项目将指定用户粉丝的详细信息爬取并存入数据库，同时也统计出有多少僵尸粉（僵尸粉的标准是我自己定的），多少真粉。由于项目目的很明确，所以扩展性并不好，对能够很好地实现对知乎粉丝信息的爬取且直观得到僵尸粉数量。📊
* 项目代码说明请看[代码解释](https://github.com/ustcyyw/zhihu_follower/blob/master/%E4%BB%A3%E7%A0%81%E8%A7%A3%E9%87%8A.md)

## 使用说明

1. 推荐将"http请求与数据库写入多线程"文件夹下所有.py文件复制并放在同一个有python环境的文件夹下面。
2. 配置自己的数据库，要求请看[数据库表格介绍]([https://github.com/ustcyyw/zhihu_follower/blob/master/%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8%E6%A0%BC%E8%AF%B4%E6%98%8E/%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8%E6%A0%BC%E4%BB%8B%E7%BB%8D.md](https://github.com/ustcyyw/zhihu_follower/blob/master/数据库表格说明/数据库表格介绍.md))。按该md文件中提示创建表格。
3. 进行项目配置，完成Config.py的配置。具体配置方案/方法请看 [配置说明](https://github.com/ustcyyw/zhihu_follower/blob/master/%E9%85%8D%E7%BD%AE%E8%AF%B4%E6%98%8E.md)。
4. 运行参数的获取，也就是main.py中main函数的参数，获取方式请看 [配置说明](https://github.com/ustcyyw/zhihu_follower/blob/master/%E9%85%8D%E7%BD%AE%E8%AF%B4%E6%98%8E.md)中关于运行参数的说明。
5. 然后你就可以愉快地运行啦 🉑

## 结果展示

* 汇总信息展示：

![汇总信息展示.png](https://github.com/ustcyyw/zhihu_follower/blob/master/%E6%96%87%E6%A1%A3%E8%BE%85%E5%8A%A9%E5%9B%BE%E7%89%87/%E6%B1%87%E6%80%BB%E4%BF%A1%E6%81%AF%E5%B1%95%E7%A4%BA.png?raw=true)

没有打码的就是我本人~

* 用户粉丝详细信息展示：

![用户粉丝详细信息展示.png](https://github.com/ustcyyw/zhihu_follower/blob/master/%E6%96%87%E6%A1%A3%E8%BE%85%E5%8A%A9%E5%9B%BE%E7%89%87/%E7%94%A8%E6%88%B7%E7%B2%89%E4%B8%9D%E8%AF%A6%E7%BB%86%E4%BF%A1%E6%81%AF%E5%B1%95%E7%A4%BA.png?raw=true)

本人早期粉丝的质量还是很高的，没有僵尸粉！

## 其它

* 如果觉得有用有意思的话给我一个star吧,请随意fork。
* 欢迎讨论与指正 微信Y154578009 /QQ154578009
* 本项目不涉及对数据的其它使用，仅仅出于个人兴趣与好奇。