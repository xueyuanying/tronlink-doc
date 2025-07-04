---
title: 开始开发
layout: docs
category: dapp
parent: dapp
---

本文档将以最简单易懂的方式指导你的 DApp 与 TronLink 应用程序相连接。

在DApp加载完成后，TronLink 会在其中注入 `window.tronLink` 对象，

  1. 如果用户连接过此 DApp， 则可以直接获取`tronLink.tronWeb 。`

  2. 如果未连接过，则可以调用请求连接后获取。

Copy

    async function getTronWeb() {
      let tronWeb;
      if (window.tronLink.ready) {
        tronWeb = tronLink.tronWeb;
      } else {
        const res = await tronLink.request({ method: 'tron_requestAccounts' });
        if (res.code === 200) {
          tronWeb = tronLink.tronWeb;
        }
      }
      return tronWeb;
    }

获取 tronWeb 实例后，即可进行 转账签名，多签签名，消息签名等链上交互动作。

具体 tronWeb 实例的使用，可参考以下文档：[](https://tronweb.network/docu/docs/intro/)

参考：[](https://developers.tron.network/docs/introduction)

[Previous用户主动连接网站消息](https://docs-zh.tronlink.org/cha-jian-qian-bao/bei-dong-jie-shou-tronlink-cha-jian-de-xiao-xi/ji-jiang-fei-qi-de-xiao-xi/yong-hu-zhu-dong-lian-jie-wang-zhan-xiao-xi)[Next多签转账](https://docs-zh.tronlink.org/dapp/duo-qian-zhuan-zhang)

Last updated 1 month ago