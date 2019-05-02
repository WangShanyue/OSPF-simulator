# 实验：模拟OSPF

## 实验内容

i. 要求学生掌握利用Socket进行编程的技术

ii. 产生4个进程，每个进程代表一个路由器，保存有自己的路由表

iii. 网络的拓扑如下

![1555402367478](C:\Users\14669\AppData\Roaming\Typora\typora-user-images\1555402367478.png)

iv. 每隔1分钟，进程交换自己的路由表

v. 可以人工输入网络之间的“距离”✔

vi. 必须使用图形界面，显示双方的语录

vii. 必须展示出谁和谁是最短路径树上是连通的，如果能够画出拓扑图更好

viii. 每一步必须显示找到了哪一个节点，本节点到它有多远，调整了的其他节点的信息（距离）

ix. 展示最新的路由表

## OSPF算法

![1555403521812](C:\Users\14669\AppData\Roaming\Typora\typora-user-images\1555403521812.png)



图形界面大概就这样

## TODO：

### 1.输出

每个进程需要输出收到了谁的链路状态，点开之后会显示一张表（这里称为链状表），表示我收到了谁的状态，

### 2.洪泛法

发送数据，可以用socket编程，首先把自己的链状表发送出去，遍历和自己相邻的结点，

接收数据，收到数据之后向发过来的链状表之后，找自己不相邻的，加到表里，同时把自己也加上，之后执行dj算法

### 3.界面设计

传输动画过程中无法暂停

传输完毕后停顿一秒，这时候可以点暂停



## 设计

### 数据结构：

1.首先要有个链状表，每个进程都有这个，这是用来进行dj的基础

表格中存的信息至少有两个： 目标路由器ID，连的结点以及距离

2.自己的标识：

ID 连的结点以及距离



### 交互：

套接字编程，同时每个进程中开两个线程

1.发送消息

发送自己已经做好的数据报，每隔一秒发一次

2.接收消息

接收外面传来的数据报，一直接收



### 界面：

![1555692452547](C:\Users\14669\AppData\Roaming\Typora\typora-user-images\1555692452547.png)

实现的要求：

可以人工输入距离

点开之后弹出个新窗口，可以显示拓扑路径

设置发送间隔时间



1.窗口

2.图形









## 实现

1. 首先用socket 创建两个进程，实现两个进程的通信

   1.1 首先创建两个进程

   1.2 socket编程实现通信

2. 现在可以进程之间收发了，但是遇到的问题就是我不能按一定时间发多条信息，不知道该怎么办

   我的思路是过一段时间产生一个进程，但是不知道为啥他

   

   

   按钮按下之后弹出窗口，把本线程的信号放进去，这样就会生成一系列的图形

   

   

### 现在有了新的方案

主线程：负责界面刷新，防止界面假死
子线程1：监听某个端口，等待连接
子线程2：用于向外连接另个路由器

子线程1每收到一个建立连接请求
就再开一个子线程3,4,5....n
分别去和一个连接请求交互

子线程1仅负责监听，并分发到新线程去
子线程2仅用于自身去向外发出连接请求
子线程3,4,5....n由子线程1产生

那么 实现的话

首先在Threads文件里定义几个新的线程，前两个保留。

主线程用来刷新界面

线程1：接收端，那就是我们这个的server了。收到消息就开一个新的线程345…… 交给他们去接收信息

线程2： 向外连接服务器，那就是我们的client端，不用修改什么东西

线程3 4 5 …… 就是用来一对一接收的





### 时刻提醒自己：不要为了分数和时间而做，而是为了学习更多的东西



###  界面设计

现在主要面临的问题就是：

1. 如何把对应的输出显示到界面上,这里可以用进程间通信的机制，所以socket其实是个不错的选择，我也成功实现了（✔） 现在需要做的就是像之前实现的那样，接收端改为多线程。（✔）

2. 如何把我们接收到的东西通过信号和槽的方式输出到界面上（✔）
3. 如何用按钮启动一个新的窗口，如果窗口不行可以打开一个messagebox

4. 如何加载图片，这个可以参考QT教程
5. 选做：从文件读取数据



### 需要修改的地方

1. 需要用个类来存对应的数据 而不是用list，那样太麻烦了
2. 可以参考观察者模式来修改自己的架构
3. 按键发送与修改数据的功能也需要实现一下

