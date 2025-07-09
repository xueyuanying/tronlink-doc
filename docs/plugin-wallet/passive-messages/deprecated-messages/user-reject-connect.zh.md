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

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FDKEjxSUrX3J3UCrRegzs%252FrejectWeb.png%3Falt%3Dmedia%26token%3Dc4485394-d713-4c90-8413-b1fd1af44b31&width=300&dpr=4&quality=100&sign=c0f84da4&sv=2)/

开发者可以监听此消息来获取用户拒绝连接消息

```shell

    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "rejectWeb") {
          // handler logic
          console.log('got rejectWeb event', e.data)
      }
    })
```

