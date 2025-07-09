# 用户确定连接消息

#### **DEPRECATED**

消息标识： `acceptWeb`

以下情况会产生此消息

  1. 用户确定连接消息

 ![image](../../../images/tronlink-wallet-extension_receive-messages-from-tronlink_messages-to-be-deprecated_user-accepts-connection_img_0.jpg)

开发者可以监听此消息来获取用户确定连接消息

```shell

    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "acceptWeb") {
          // handler logic
          console.log('got acceptWeb event', e.data)
      }
    })
```

