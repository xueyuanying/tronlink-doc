---
title: 网络改变消息
layout: docs
category: plugin
parent: plugin-wallet/passive-messages
---

消息标识： `setNode`

**简介**

开发者可以监听此消息来获取网络的改变

以下情况会产生此消息

  1. 用户改变网络的时候

**技术规范**

**代码示例**

Copy

    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "setNode") {
          // handler logic
          console.log('got setNode event', e.data)
      }
    })

**返回值**

Copy

    {
      "node": {
        // 当前网络的信息
      },
      "connectNode": {
        // dapp chain 的节点信息
      }
    }

[Previous账户改变消息](https://docs-zh.tronlink.org/cha-jian-qian-bao/bei-dong-jie-shou-tronlink-cha-jian-de-xiao-xi/zhang-hu-gai-bian-xiao-xi)[Next连接网站成功消息](https://docs-zh.tronlink.org/cha-jian-qian-bao/bei-dong-jie-shou-tronlink-cha-jian-de-xiao-xi/lian-jie-wang-zhan-cheng-gong-xiao-xi)

Last updated 2 years ago