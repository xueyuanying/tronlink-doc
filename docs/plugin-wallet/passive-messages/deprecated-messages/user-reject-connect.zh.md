---
title: 用户拒绝连接消息
layout: docs
category: plugin
parent: plugin-wallet/passive-messages/deprecated-messages
---

#### **DEPRECATED**

消息标识： `rejectWeb`

以下情况会产生此消息：

  1. DApp 请求连接，用户在弹窗中拒绝连接后

![image](../../../images/tronlink-wallet-extension_receive-messages-from-tronlink_messages-to-be-deprecated_user-rejects-connection_img_0.jpg)

开发者可以监听此消息来获取用户拒绝连接消息

```shell

    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "rejectWeb") {
          // handler logic
          console.log('got rejectWeb event', e.data)
      }
    })
```

