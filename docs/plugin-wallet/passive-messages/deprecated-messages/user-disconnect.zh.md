# 用户断连网站消息

<span class="deprecated">DEPRECATED</span>

消息标识： `disconnectWeb`

以下情况会产生此消息

  1. 用户主动断接网站

![image](../../../images/tronlink-wallet-extension_receive-messages-from-tronlink_messages-to-be-deprecated_user-disconnects-from-the-website_img_0.jpg)

开发者可以监听此消息来获取用户主动断连消息

```shell

    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "disconnectWeb") {
          // handler logic
          console.log('got disconnectWeb event', e.data)
      }
    })
```

