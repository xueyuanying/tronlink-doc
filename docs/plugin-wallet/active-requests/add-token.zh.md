---
title: 添加Token
layout: docs
category: plugin
parent: plugin-wallet/active-requests
---

**简介**

DApp 提供按钮给用户， 直接将指定的 Token 添加到用户插件的资产展示列表中。

**技术规范**

**代码示例**

```shell

    const res = await tronWeb.request({
      method: 'wallet_watchAsset',
      params: {
        type: 'TRC20',
        options: {
            address: 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t'
        }
      },
    });
```
**参数**

```shell

    interface WatchAssetParams {
      type: 'trc10' | 'trc20' | 'trc721';
      options: {
        address: string;
        symbol?: string;
        decimals?: number;
        image?: string;
      }
    }
```
  * method: wallet_watchAsset 固定的字符串

  * params: WatchAssetParams，具体参数如下：

    * type: 目前只支持 'trc10', 'trc20', 'trc721' 三种

    * options:

      * address: token 的合约地址 或者 token id, 必传

      * symbol: 占位(目前未使用)，可选

      * decimals: 占位(目前未使用)，可选

      * image: 占位(目前未使用)，可选

**返回值**

此方法没有返回值

**交互流程**

**添加 TRC10 资产**

```shell

    if (window.tronLink.ready) {
      const tronweb = tronLink.tronWeb;
      try {
        tronweb.request({
          method: 'wallet_watchAsset',
          params: {
            type: 'trc10',
            options: {
              address: '1002000'
            },
          },
        });
      } catch (e) {}
    }
```
代码执行时，TronLink 会弹出添加窗口，用户点击确定添加 TRC10 资产，或者取消添加。

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FrSMt7NQmXzMuTPkiT9O1%252Fadd_trc10.png%3Falt%3Dmedia%26token%3D5db66668-177c-42ec-94e9-e6cc5b3b370a&width=300&dpr=4&quality=100&sign=6e819ebe&sv=2)

点击“添加”按钮，资产被添加到资产列表，如下图所示：

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FI1ct7TLiGNkecTmcqEE1%252Fadd_trc10_success.png%3Falt%3Dmedia%26token%3Da8cb24fd-ee54-42f5-a75d-6517b2f5c636&width=300&dpr=4&quality=100&sign=ef3f6b70&sv=2)

**添加 TRC20 资产**

```shell

    if (window.tronLink.ready) {
      const tronweb = tronLink.tronWeb;
      try {
        tronweb.request({
          method: 'wallet_watchAsset',
          params: {
            type: 'trc20',
            options: {
              address: 'TF17BgPaZYbz8oxbjhriubPDsA7ArKoLX3'
            },
          },
        });
      } catch (e) {}
    }
```
代码执行时，TronLink 会弹出添加窗口，用户点击确定添加 TRC20 资产，或者取消添加。

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FKU96R8jtqXTZjBmwX685%252Fadd_trc20.png%3Falt%3Dmedia%26token%3D278c33aa-2288-497a-b0c3-3b6f192ca747&width=300&dpr=4&quality=100&sign=9bee926&sv=2)

点击“添加”按钮，资产被添加到资产列表，如下图所示：

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FL8enI9M8SNOdCVQxAWWL%252Fadd_trc20_success.png%3Falt%3Dmedia%26token%3D7da90361-8cb6-48ea-91cb-bedd13a34ed0&width=300&dpr=4&quality=100&sign=25bda2d9&sv=2)

**添加 TRC721 资产**

```shell

    if (window.tronLink.ready) {
      const tronweb = tronLink.tronWeb;
      try {
        tronweb.request({
          method: 'wallet_watchAsset',
          params: {
            type: 'trc721',
            options: {
              address: 'TVtaUnsgKXhTfqSFRnHCsSXzPiXmm53nZt'
            },
          },
        });
      } catch (e) {}
    }
```
代码执行时，TronLink 会弹出添加窗口，用户点击确定添加 TRC721 资产，或者取消添加。

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FfQ6V6sFbIdibHoNi0DzN%252Fadd_trc721.png%3Falt%3Dmedia%26token%3D49fd8ed2-6081-4bb4-ab10-f307ad3f30b6&width=300&dpr=4&quality=100&sign=eeb41a63&sv=2)

点击”添加”按钮，资产被添加到资产列表，如下图所示：

![](https://docs-zh.tronlink.org/~gitbook/image?url=https%3A%2F%2F1166523713-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCXoQmcUHNY97twQ2Y2PY%252Fuploads%252FfQ6V6sFbIdibHoNi0DzN%252Fadd_trc721.png%3Falt%3Dmedia%26token%3D49fd8ed2-6081-4bb4-ab10-f307ad3f30b6&width=300&dpr=4&quality=100&sign=eeb41a63&sv=2)

[Previous连接网站](https://docs-zh.tronlink.org/cha-jian-qian-bao/zhu-dong-qing-qiu-tronlink-cha-jian-gong-neng/lian-jie-wang-zhan)[Next被动接收TronLink插件的消息](https://docs-zh.tronlink.org/cha-jian-qian-bao/bei-dong-jie-shou-tronlink-cha-jian-de-xiao-xi)

