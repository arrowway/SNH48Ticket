# SNH48官方商城门票捡漏
![alt](https://img.shields.io/badge/Python-2.7-brightgreen.svg)

### SNH48Ticket 是一个用于SNH48官方商城的切票捡漏脚本

查询余票，自动下单，多线程请求

妈妈再也不用担心我切不到票啦！

声明：本脚本只做学习交流使用，请勿用于其他用途

|Author|莽夫|
|---|---
|URL|https://github.com/DipperStar/SNH48Ticket

## 使用方法

* 主函数
```Python
if __name__ == '__main__':
    urllib.getproxies_registry = lambda : {}
    se = ORDER('username','password','ticketcode','seattype','brandid','teamtype')
    for i in range(30):
        th = threading.Thread(target=se.ticket)
        th.start()
```
* 参数说明：

    以下参数均为字符型
    
    |变量名|username|password|ticketcode|seattype|brandid|teamtype
    |---|---|---|---|---|---|---
    |说明|用户名|密码|门票编号|门票类型|团体编号|队伍编号
    
    各编号对应表：

    |团体|SNH|BEJ|GNZ|SHY|CKG|
    |---|---|---|---|---|---
    |brandid|1|2|3|4|5

    |队伍|G|N3|Z|
    |---|---|---|---
    |teamtype|0|1|3

    |门票类型|VIP|普|站|
    |---|---|---|---
    |门票编号|2|3|4

    门票编号获取方式：

    切票页面地址最后四位数字编码即为门票编号
    ![图片显示失败](https://wx2.sinaimg.cn/mw690/853af3eegy1fn2pathyl7j20nf0ia7cm.jpg)

    * 如何开始

        填写好必要参数后，在命令行输入python Ticket.py运行脚本

    * 切票流程

    1.开始运行脚本后会弹出chrome窗口，跳转到48会员登录页面，自动输入账号密码并点击登录
    ![图片显示失败](https://wx2.sinaimg.cn/mw690/853af3eegy1fn2pathszbj20le0e3wgf.jpg)

    2.登录成功后，会自动弹出48商城页面，脚本获取cookie后会自动关闭chrome窗口，到此完成模拟登录。
    ![图片显示失败](https://wx4.sinaimg.cn/mw690/853af3eegy1fn2patmfryj210o0k71kx.jpg)

    3.脚本开始自动捡漏，只需耐心等待，每次下单成功，会print order succeed...，此时可前往商城订单页面查看是否抢到门票
## 流程框图



## 更新日志
    [2018.01.02]

    * 修复查询余票的bug，解析方式从eval改为json

    [2017.12.28]

    * 增加post中的choose_times_end字段
    * 更新查询余票的接口地址

    [2017.11.21]

    * 增加超V出价功能

    [2017.10.21]

    * 增加GUI

    [2017.10.20]

    * 增加浏览器模拟登录，依赖chromedriver

    [2017.5.30]

    * 增加多线程请求方式

    [2017.5.24] 

    * 增加查询库存模块的容错，取消是否在架判断，优化库存满足时的条件判断速度

    [2017.5.22]

    * 基本查询，下单功能

## 关联库：

![alt](https://img.shields.io/badge/requests--green.svg) ![alt](https://img.shields.io/badge/selenium--yellowgreen.svg)
