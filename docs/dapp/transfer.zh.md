---
title: 普通转账
layout: docs
category: dapp
parent: dapp
---

**简介**

DApp 需要用户发起一笔 TRX 转账。

前提: DApp 开发者完成连接网站请求，用户同意连接。

波场网络上发起转账需要3个步骤：

  1. 构造转账交易

  2. 对交易进行签名

  3. 对签名后的交易进行广播

在这里，TronLink 介入的是第2步签名的部分，1, 3 两步需要开发者使用 tronWeb 完成

**技术规范**

**代码示例**

```shell 
    if (window.tronLink.ready) {
      const tronweb = tronLink.tronWeb;
      const fromAddress = tronweb.defaultAddress.base58;
      const toAddress = "TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ";
      const tx = await tronweb.transactionBuilder.sendTrx(toAddress, 10, fromAddress); // 步骤1
      try {
        const signedTx = await tronweb.trx.sign(tx); // 步骤2
        await tronweb.trx.sendRawTransaction(signedTx); // 步骤3
      } catch (e) {
        // error handling
      }
    }
```

当代码执行到`await tronweb.trx.sign(tx);`时，TronLink钱包会提示弹窗，需要用户进行确认，如下图：

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FsPt6RFvrdpaQr2bC04Xv%252Fsign_trx.png%3Falt%3Dmedia%26token%3D91dbf461-f487-4c08-92ef-2e5efba694ce&width=300&dpr=4&quality=100&sign=60edce58&sv=2)

如果用户在弹窗中选择【拒绝】，则会抛出异常，开发者可捕获此异常进行业务处理。

如果用户在弹窗中选择【签名】，DApp 可以拿到签名后的交易，继续进行广播。

