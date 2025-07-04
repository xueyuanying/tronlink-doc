---
title: 打开DApp
layout: docs
category: mobile
parent: mobile/deeplink
---

### 使用 DeepLink 方式唤起钱包，并在 DApp 浏览器中打开 DApp

Copy

    // Tronlink-v4.10.0
    // 链接
    Open DApp

Copy

    // param的参数为json格式的协议数据
    // 注意：json.toString后需要进行urlencode编码
    {
    	"url": "https://www.tronlink.org/", //目标DApp
    	"action": "open",
    	"protocol": "tronlink",
    	"version": "1.0"
    }

[Previous打开钱包](https://docs-zh.tronlink.org/yi-dong-duan/deeplink/da-kai-qian-bao)[Next登陆授权](https://docs-zh.tronlink.org/yi-dong-duan/deeplink/deng-lu-shou-quan)

Last updated 2 years ago