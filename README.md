这几天除了工作外，忙活的微信里面的一个投票栏目，简单描述如下：

###背景

双11将临，女人最离不开互联网的时候到了。家里狗狗没狗粮了，老婆不知从哪得到的一个宠物投票应用，反正就是上传自己宠物图片，浏览者进行投票，票数高的奖励狗粮之类的。然后，就把链接放到我们自己人群里面（4个人）让大家一起帮忙投票，看了下第一名已经三百多票，差的远。我多嘴说了一句“我写个程序来刷票吧”，他们几个表示很惊讶（非常的不信），不是程序员的我海口已经夸下，之前从没这样搞过(T_T)，于是开始了

###实现原理

1. 微信投票过程

* 微信上一个链接，点开跳转到第三方网站（具体哪个网站就不说了），进行微信授权后进入了投票界面，找到我们上传的狗狗照片上有个投票点击则投票，则票数增加1
* 整个过程除了微信授权，没有任何验证码！（猜程序员小哥可能是怕麻烦没人参加，但是刷票难度大大降低）
* 一个人可多次投票，间隔5分钟左右
   
2. Chrome过程分析

* 拷贝投票界面网址，在Chrome可以打开！（网址带有微信授权的openid，没加密!）
* 使用开发者模式监测投票过程，发现是以post形式，数据为openid及要投票的图片ID
* 试着直接修改浏览器地址的openid进行投票，服务器反馈微信参数错误，猜到是每个微信号授权后获取的唯一openid存在它们服务器进行投票验证，非法openid不能投票，fxxk！程序员小哥还防刷票呢
* 我让别人给我授权后的投票网址，由于是合法的openid，可以投票，因此可以刷票了，问题在于能获取多少openid，则能刷多快
   
3. 代码实现

* 为了方便移植（能在别的电脑上跑程序），没有使用第三方轮子
* 之前玩过爬虫，首选程序核心为urllib模块，进行网页的交互
* 其他使用了随机、延时、字典、列表，具体见程序源码
* 不同的狗狗只要更改狗狗图片ID即可
   
![image](https://github.com/Stev00/wechat_vote/blob/master/Pic/voting_process.png)
   
* 18个openid，80多行代码搞定！
   
###结果

1. 当然，肯定的刷到了第一位置，哈哈
   
![image](https://github.com/Stev00/wechat_vote/blob/master/Pic/see_web.png)
   
2. 上面图片第一个是我上传的狗狗图片，在前十即可。票数排第一的是老婆发布的金毛
3. 截至时间是本月底，继续刷吧，狗狗的口粮就快到手了...
4. 女人这种生物，真的好麻烦
