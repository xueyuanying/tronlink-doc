---
title: 打开钱包
layout: docs
category: mobile
parent: mobile/deeplink
---

### 使用 DeepLink 方式唤起钱包

Copy

    // Tronlink-v4.10.0
    // 链接
    Open Tronlink

Copy

    // param的参数为json格式的协议数据
    // 注意：json.toString后需要进行urlencode编码
    {
    	"action": "open",
    	"protocol": "tronlink",
    	"version": "1.0"
    }

[PreviousDeepLink](https://docs-zh.tronlink.org/yi-dong-duan/deeplink)[Next打开DApp](https://docs-zh.tronlink.org/yi-dong-duan/deeplink/da-kai-dapp)

Last updated 2 years ago