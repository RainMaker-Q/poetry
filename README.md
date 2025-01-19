# poetry
抓取莎士比亚的十四行诗。

## 前言
想做个莎士比亚文风的机器人，先爬取点数据，这里是十四行诗的内容。

## 方案
在 [这里]('https://web.archive.org/web/20140320160055/http://shashibiya.org/sonnet-no-1/')找到了莎士比亚的文章，但是发现国内连接超市访问不到（你懂得）。这里用cf做了一层代理，进行转发。

本机 <=> cloud flare <=> 目标站

## 数据内容
整理了每一章的页面链接，和数据内容，还拆分了结构。需要自取。
有一些数据不太干净，后面再完善写。

做了个后台，管理下数据，后面调整个H5承接页，随机一首诗，也可以接入到每日一句中。

![列表]('https://github.com/RainMaker-Q/picture/blob/master/poetry_list.jpg?raw=true')
![详情]('https://github.com/RainMaker-Q/picture/blob/master/poetry_detail.jpg?raw=true')
