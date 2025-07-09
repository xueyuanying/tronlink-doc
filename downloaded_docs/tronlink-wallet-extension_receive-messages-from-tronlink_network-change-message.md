  1. [TronLink Wallet Extension](/tronlink-wallet-extension)
  2. [Receive messages from TronLink](/tronlink-wallet-extension/receive-messages-from-tronlink)



# Network Change Message

Message ID: `setNode`

**Overview**

Developers can monitor this message to know network changes This message is generated when:

  1. When the user changes the network




**Specification**

**Example**

Copy
    
    
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "setNode") {
        // handler logic
        console.log('got setNode event', e.data)
      }
    })

**Returns**

Copy
    
    
    {
      "node": {
        // Information about the current network
      },
      "connectNode": {
        // Node information of DApp chain
      }
    }

[PreviousAccount Change Message](/tronlink-wallet-extension/receive-messages-from-tronlink/account-change-message)[NextSuccessful connection message](/tronlink-wallet-extension/receive-messages-from-tronlink/successful-connection-message)

Last updated 2 years ago
