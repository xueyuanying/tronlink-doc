---
title: 用户断连网站消息
layout: docs
category: plugin
parent: plugin-wallet/passive-messages/deprecated-messages
---

#### **DEPRECATED**

消息标识： `disconnectWeb`

以下情况会产生此消息

  1. 用户主动断接网站

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FbjCWnFVkxhg5X5RVYJhK%252FdisconnectWeb.png%3Falt%3Dmedia%26token%3Ddca1c604-6316-4665-810c-71434143f6ad&width=300&dpr=4&quality=100&sign=92065387&sv=2)

开发者可以监听此消息来获取用户主动断连消息

Copy

    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "disconnectWeb") {
          // handler logic
          console.log('got disconnectWeb event', e.data)
      }
    })

[Previous用户拒绝连接消息](https://docs-zh.tronlink.org/cha-jian-qian-bao/bei-dong-jie-shou-tronlink-cha-jian-de-xiao-xi/ji-jiang-fei-qi-de-xiao-xi/yong-hu-ju-jue-lian-jie-xiao-xi)[Next用户确定连接消息](https://docs-zh.tronlink.org/cha-jian-qian-bao/bei-dong-jie-shou-tronlink-cha-jian-de-xiao-xi/ji-jiang-fei-qi-de-xiao-xi/yong-hu-que-ding-lian-jie-xiao-xi)

Last updated 2 years ago