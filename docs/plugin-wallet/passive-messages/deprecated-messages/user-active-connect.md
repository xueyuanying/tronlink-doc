---
title: 用户主动连接网站消息
layout: docs
category: plugin
parent: plugin-wallet/passive-messages/deprecated-messages
---

#### **DEPRECATED**

消息标识： `connectWeb`

以下情况会产生此消息

  1. 用户确定连接消息

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FBGG5V16Vw9K3uDXAKrDm%252FconnectWeb.png%3Falt%3Dmedia%26token%3D29562e27-c8ef-44aa-b6b6-d69cba9f7709&width=300&dpr=4&quality=100&sign=5c2c5c7b&sv=2)

开发者可以监听此消息来获取用户主动连接网站消息

Copy

    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "connectWeb") {
          // handler logic
          console.log('got connectWeb event', e.data)
      }
    })

[Previous用户确定连接消息](https://docs-zh.tronlink.org/cha-jian-qian-bao/bei-dong-jie-shou-tronlink-cha-jian-de-xiao-xi/ji-jiang-fei-qi-de-xiao-xi/yong-hu-que-ding-lian-jie-xiao-xi)[Next开始开发](https://docs-zh.tronlink.org/dapp/kai-shi-kai-fa)

Last updated 2 years ago