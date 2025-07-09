# Stake2.0

When generating stake 2.0 transactions for DApps, for transactions of the `DelegateResourceContract` or `UnDelegateResourceContract` type, in order to display the estimated results during signature using the Tronlink extension, it is necessary to add the "__options" field to the transaction body.

Inside "__options", there are two values: estimatedBandwidth and estimatedEnergy, which correspond to the estimated energy and bandwidth of the delegate and reclaim operations, respectively.

When generating stake 2.0 transactions using a non-tronlink extension injected tronweb, in order to display the corresponding type of resource for `DelegateResourceContract` or `UnDelegateResourceContract` type transactions during signature, the "__resource" field needs to be added to the transaction body. (Adding “resource” is only necessary for tronWeb that is not injected by a tronlink extension. TronWeb that is injected by tronlink extension does not require.)

The "__resource" field corresponds to the values "BANDWIDTH" and "ENERGY".

![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252FsrTq5GWES6Pys74GW6pY%252Fimage.png%3Falt%3Dmedia%26token%3D13f5fcdd-daba-42a0-8bc8-de93c6b745ee&width=768&dpr=4&quality=100&sign=3c7442&sv=2)

For example:

```shell 
    const transaction = await tronWeb.transactionBuilder.delegateResource(10e6, 'receiverAddress', 'BANDWIDTH', 'ownerAddress', false);
    transaction.raw_data.contract[0].parameter.value.resource = "BANDWIDTH"
    transaction.__options = {"estimatedBandwidth": 1}
```

The specific calculation logic of estimatedEnergy and estimatedBandwidth can be found in the last chapter of the "[Stake 2.0 Adaptation FAQ](https://coredevs.medium.com/stake-2-0-adaption-faq-66bafdf53606)": "How to convert resource share to amount?"

