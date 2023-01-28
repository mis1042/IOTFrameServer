# 基于Python实现的物联网框架-服务端
## 注意，这个框架还没有准备好投入使用！！！甚至客户端都还在写（新建文件夹）
## 快速开始
### Step0：准备服务端依赖
```shell
pip3 install rsa
```
### Step1：初始化您的服务端配置
1.生成RSA密钥（方法很多，举个例子）
```python
import rsa
(pubkey, privkey) = rsa.newkeys(1024)
print(pubkey.save_pkcs1().decode('utf-8'))
print(privkey.save_pkcs1().decode('utf-8'))
```
2.将生成的公钥和私钥填入`server.json`中  
3.给你的服务器起一个名字（ServerName选项）  
4.编辑连接地址与端口号（hostname和Port）
### Step2：创建您的第一个设备
找到tools/device_creator.py，直接运行即可
根据提示输入设备ID，然后在当前目录会生成客户端配置文件，将其复制到客户端目录下即可  
**注意事项**
1.您可能需要修改客户端配置文件以正确连接到服务端（只修改hostname和Port)  
2.不要把服务端或者客户端的配置文件直接发给别人！！！  
3.不要把服务端或者客户端的配置文件直接发给别人！！！  
4.不要把服务端或者客户端的配置文件直接发给别人！！！  
服务端的私钥泄漏可能面临中间人伪造服务端  
客户端的私钥泄漏将导致Device.PrivateSend方法不再安全  
### Step3：启动您的服务端
```shell
python3 main.py
```
## 开发教程：  
参见本项目Wiki

## 许可协议
有附加要求的MIT许可证（见LICENSE文件）

## 鸣谢
https://blog.csdn.net/weixin_42066185/article/details/106670921  
https://blog.csdn.net/QQ_1993445592/article/details/102578595  
两位作者提供的线程停止和AES加密代码

[Jetbrains](https://www.jetbrains.com/)所提供的PyCharm Professional For Student开发工具

本项目的所有依赖库的提供

以及所有帮助过我开发该项目的人

## 赞助

唯一的赞助方式：  

作者最希望的是所有人（无论性取向和性别认同如何）都能在世间被平等，温柔地对待  
性少数不是疾病，更不是心理变态，呼吁停止一切的非法矫正行为，这只会伤害无辜  
如果正在阅读这篇README的你也是少数群体，永远记住————  
无论取向与认同如何，永远记住，我们永远不是天生低人一等的，我们与其他所有人一样  

[如果你能记住我的名字，如果你们都能记住我的名字，也许我或者“我们”，终有一天能自由地生存着。](https://github.com/mtf-wiki/MtF-wiki)
