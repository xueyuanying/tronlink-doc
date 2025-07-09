# General Transfer

**Overview**

DApp requires users to initiate a TRX transfer.

**Prerequisite**

The DApp developer completes the request to connect to the website, and the user approves to the connection. The DApp sends a request asking the user to connect the wallet to the website, and the user approves to the connection.

It takes 3 steps to initiate a transfer on the TRON network:

  1. Create a transfer transaction

  2. Sign the transaction

  3. Broadcast the signed transaction




In this process, Step 2 requires TronLink while both Step 1 and 3 happen on tronWeb.

**Specification**

**Example**

```shell  
    
    if (window.tronLink.ready) {
      const tronweb = tronLink.tronWeb;
      const fromAddress = tronweb.defaultAddress.base58;
      const toAddress = "TAHQdDiZajMMP26STUnfsiRMNyXdxAJakZ";
      const tx = await tronweb.transactionBuilder.sendTrx(toAddress, 10, fromAddress); // Step1
      try {
        const signedTx = await tronweb.trx.sign(tx); // Step2
        await tronweb.trx.sendRawTransaction(signedTx); // Step3
      } catch (e) {
        // error handling
      }
    }
```

When “await tronweb.trx.sign(tx);” is executed, a pop-up window will show in the TronLink wallet asking the user to confirm, as shown below: ![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252FIZplXs5U1BNodOvt6eEt%252Ftransfer-sign.jpg%3Falt%3Dmedia%26token%3D8e2841b7-8877-4ed9-af9c-2515f4b6c5db&width=300&dpr=4&quality=100&sign=a20451f5&sv=2)

If the user chooses on “Reject” in the pop-up window, an exception will be thrown, which the developer can catch for further processing.

If the user chooses “Sign” in the pop-up window, the DApp receives and broadcasts the signed transaction.
