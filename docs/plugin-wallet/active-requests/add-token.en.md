# Add Token

**Overview**

Buttons on DApps allow users to directly add the specified tokens to the asset list on their TronLink user extension.

**Specification**

**Example**

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
**Parameters**

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
  * method: wallet_watchAsset fixed string

  * params: WatchAssetParams, the specific parameters are as follows:

  * type: Only 'trc10', 'trc20', 'trc721' are supported now

  * options:

  * address: the contract address of the token or the token id, required

  * symbol: placeholder (currently unused), optional

  * decimals: placeholder (currently unused), optional

  * image: placeholder (currently unused), optional


**Returns**

This method has no return value

**Interaction**

**Add TRC10 assets**

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

When the code is executed, a TronLink pop-up window for adding TRC10 assets will show up, and the user can click “Add” or “Cancel”. ![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252FwRtbA3NjBdF3IG0A6Dbl%252Fadd-TRC10-token.jpg%3Falt%3Dmedia%26token%3Db3175131-1ca5-4910-98f6-cf656ea475ab&width=300&dpr=4&quality=100&sign=74e9b0dc&sv=2)

After clicking "Add", users can see the added assets as shown in the following screen:

![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252FRCkzoYq278Vtv42gFGY3%252Fadd-TRC10-token-after.jpg%3Falt%3Dmedia%26token%3D546b862f-3e20-44e9-9fcd-6c362aac693d&width=300&dpr=4&quality=100&sign=b2d3cf25&sv=2)

**Add TRC20 assets**

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
When the code is executed, a TronLink pop-up window for adding TRC20 assets will show up, and the user can click “Add” or “Cancel”. ![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252FPkxxQDg6AeJp2DEgSyhB%252Fadd-TRC20-token.jpg%3Falt%3Dmedia%26token%3D97301a6f-8f39-4bf2-ae13-a361364e581d&width=300&dpr=4&quality=100&sign=ff1355ec&sv=2)

After clicking “Add”, users can see the added assets as shown in the following screen: ![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252FWGYD0QmzqHigFuXkGYmP%252Fadd-TRC20-token-after.jpg%3Falt%3Dmedia%26token%3Df493cee0-e4d0-431c-960b-1971e48f6db2&width=300&dpr=4&quality=100&sign=2219fd9e&sv=2)

**Add TRC721 asset**

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
When the code is executed, a TronLink pop-up window for adding TRC721 will show up, and the user can click “Add” or “Cancel”. ![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252FHstgtwLQmdRS7grGQ5H0%252Fadd-TRC721-token.jpg%3Falt%3Dmedia%26token%3Da129ebf9-1c9b-4909-bb0f-a0f567b02869&width=300&dpr=4&quality=100&sign=166eb4a8&sv=2)

After clicking “Add”, users can see the added assets as shown in the following screen: ![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252FzRoSUMQ7EtK1eKMmZOS9%252Fadd-TRC721-token-after.jpg%3Falt%3Dmedia%26token%3Dea5afa9a-1cdd-46db-bd96-20822b85f9a7&width=300&dpr=4&quality=100&sign=4904733c&sv=2)
