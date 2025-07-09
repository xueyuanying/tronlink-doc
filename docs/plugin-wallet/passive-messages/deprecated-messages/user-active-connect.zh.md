# 用户主动连接网站消息

#### <span class="deprecated">DEPRECATED</span>

消息标识： `connectWeb`

以下情况会产生此消息

  1. 用户确定连接消息

![image](../../../images/tronlink-wallet-extension_receive-messages-from-tronlink_messages-to-be-deprecated_user-requests-to-connect-to-the-website_img_0.jpg)

开发者可以监听此消息来获取用户主动连接网站消息

```shell

    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "connectWeb") {
          // handler logic
          console.log('got connectWeb event', e.data)
      }
    })
```

