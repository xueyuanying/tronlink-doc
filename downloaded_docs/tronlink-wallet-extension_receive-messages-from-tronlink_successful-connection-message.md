  1. [TronLink Wallet Extension](/tronlink-wallet-extension)
  2. [Receive messages from TronLink](/tronlink-wallet-extension/receive-messages-from-tronlink)



# Successful connection message

Message ID: `connect`

**Overview**

Developers can monitor this message for connection changes. This message is generated when:

  1. The DApp requests a connection, and the user confirms the connection in the pop-up window

  2. Users connect to the website




**Specification**

**Example**

Copy
    
    
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "connect") {
        // handler logic
        console.log('got connect event', e.data)
      }
    })

[PreviousNetwork Change Message](/tronlink-wallet-extension/receive-messages-from-tronlink/network-change-message)[NextDisconnect website message](/tronlink-wallet-extension/receive-messages-from-tronlink/disconnect-website-message)

Last updated 2 years ago
