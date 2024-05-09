# Youkat_UploadFileVul_EXP
优卡特脸爱云管理系统存在文件上传漏洞，被恶意利用后影响严重。
*****
## 0x01 组件介绍
脸爱云是一款智慧点餐管理平台，帮助企业实现智能化管理、云端部署，并提供安全保障和定制化服务，助力企业提升管理水平和竞争力。

该产品广泛应用于餐馆点餐或校企机构刷脸点单，该平台 /UpLoadPic.ashx接口处存在文件上传漏洞，未对传入文件参数进行鉴权,导致未经身份认证的攻击者可以通过此漏洞构造参数上传文件，造成后续服务器接管，具有较严重的影响后果。

**声明**：本EXP仅用于自检，如若因为其他原因造成危害，本人概不负责！
## 0x02 使用方法
### 资产测绘

FOFA:title=="欢迎使用脸爱云 一脸通智慧管理平台"

Zoomeye:title:"欢迎使用脸爱云 一脸通智慧管理平台"

### 参数使用

python -u http://target_ip/Login.aspx

python -f file.txt
### 使用原理
  
对指定ip上传post报文构造aspx文件，并通过脚本内response.write写入数据，如若想写入其他数据，请自行修改该行。
如果上传成功，则返回存在漏洞，请自行进行后续测试。

### 使用结果
  
#### 1. 命令输入

![1715256662884(1)](https://github.com/jidle123/Youkat_UploadFileVul_EXP/assets/123531867/52db086c-433c-4f28-be04-47f659bb881b)

#### 2. 后续验证

文件上传测试如下：

![1715256762203](https://github.com/jidle123/Youkat_UploadFileVul_EXP/assets/123531867/cd22e938-c109-45b4-93c0-84d96e1b681e)

文件访问存在：

![1715256860306](https://github.com/jidle123/Youkat_UploadFileVul_EXP/assets/123531867/943c411d-9ead-4fe2-9a2b-973863f0fcc3)

