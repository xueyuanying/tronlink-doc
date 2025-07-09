---
title: 消息签名
layout: docs
category: dapp
parent: dapp
---

**简介**

DApp 需要用户对一个 hex 消息签名，签名后消息转发给后端进行验签，以此判断用户合法登陆。

**前提**

DApp 开发者完成【连接网站】请求，用户同意连接。

**技术规范**

**代码示例**

Copy

    if (window.tronLink.ready) {
      const tronweb = tronLink.tronWeb;
      try {
        const message = "0x01EF"; // any hex string
        const signedString = await tronweb.trx.sign(message);
      } catch (e) {}
    }

**参数**

`tronLink.tronWeb.trx.sign`接收一个十六进制的字符串作为参数，该字符串表示当前待签名的内容。

**返回值**

如果用户在弹窗中选择签名, DApp 可以得到签名后的十六进制字符串, 比如：

```shell 
    0xaa302ca153b10dff25b5f00a7e2f603c5916b8f6d78cdaf2122e24cab56ad39a79f60ff3916dde9761baaadea439b567475dde183ee3f8530b4cc76082b29c341c
```

如果报错，则会返回如下信息：

```shell 
    Uncaught (in promise) Invalid transaction provided
```
**交互流程**

当代码执行到`await tronweb.trx.sign(message);`时，TronLink 钱包会提示弹窗，需要用户进行确认， 如下图, 其中消息内容会以hex的方式展示：

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FJlFrpYwXQzxN7ai4fTS2%252Fsign_message.png%3Falt%3Dmedia%26token%3D1bd85477-b736-4cfc-a915-66ec0f9d064f&width=300&dpr=4&quality=100&sign=c271bad1&sv=2)

如果用户在弹窗中选择【拒绝】，则会抛出异常，开发者可捕获此异常进行业务处理。

