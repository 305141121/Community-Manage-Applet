## 配置

setting.py：
+   DATABASES
+   LOGGING 日志输出设置

## 接口说明

[user](#user)
[message](#message)
[wechat_push](#wechat_push)

<span id = "user"></span>
### user.py  
+   **login** /test/login 
小程序端发送code给服务器，服务器利用code向微信获取其openid，返回加密token，在后续操作中用来标识用户。 
*后续所有操作都应该附上此代码段与服务器交互*
```
wx.request({
          // 依据情况换成对应IP
          url: 'http://127.0.0.1:8000/test/对应接口URL/',
          header: {
            'content-type': 'application/json'          
          },
          data:{
            token: wx.getStorageSync("token"),
          },
          method: "POST",
          success: function (res) {
            console.log('success!')
            
          },
          fail: function () {
            console.log('fail!')
          }
        })
```

+   **updateUserInfo** /test/updateUserInfo
用户修改信息时，小程序端 Post 对应 name, grade, major, sex, phone 字段信息

+   **getUserInfo** /test/getUserInfo
用户在跳转到个人资料详细页面时

----------------------------
<span id = "message"></span>
### message.py
+   **getMessageCount** /test/getMessageCount
获取用户当前的未读消息数量

+   **getMessageUnread** /test/getMessageCount
获取用户的未读信息，返回json数据，需要解析对应字段content, sendtime，解析如下

```
 //获取所有消息内容          
var messages = res.data
for (var i in messages)               
    console.log(messages[i]['content'] + " " + messages[i]['sendtime'])
```

----------------------------

**wechat_push.py**
