# 基于Python实现的物联网框架-服务端

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
