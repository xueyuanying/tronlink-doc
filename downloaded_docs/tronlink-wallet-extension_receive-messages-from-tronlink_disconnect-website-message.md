  1. [TronLink Wallet Extension](/tronlink-wallet-extension)
  2. [Receive messages from TronLink](/tronlink-wallet-extension/receive-messages-from-tronlink)



# Disconnect website message

Message ID: `disconnect`

**Overview**

Developers can monitor this message for connection changes. This message is generated when:

  1. The DApp requests a connection, and the user rejects the connection in the pop-up window

  2. Users disconnect from the website




**Specification**

**Example**

Copy
    
    
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "disconnect") {
        // handler logic
        console.log('got connect event', e.data)
      }
    })

[PreviousSuccessful connection message](/tronlink-wallet-extension/receive-messages-from-tronlink/successful-connection-message)[NextMessages to Be Deprecated](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated)

Last updated 2 years ago
