---
title: 用户确定连接消息
layout: docs
category: plugin
parent: plugin-wallet/passive-messages/deprecated-messages
---

#### **DEPRECATED**

消息标识： `acceptWeb`

以下情况会产生此消息

  1. 用户确定连接消息

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FCUqxSxp5zvpWe3aCkWlh%252FacceptWeb.png%3Falt%3Dmedia%26token%3D60f79480-1e05-40a3-a36d-9415b8d8cdd8&width=300&dpr=4&quality=100&sign=f87cc77d&sv=2)

开发者可以监听此消息来获取用户确定连接消息

```shell

    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "acceptWeb") {
          // handler logic
          console.log('got acceptWeb event', e.data)
      }
    })
```

