  1. [TronLink Wallet Extension](/tronlink-wallet-extension)
  2. [Receive messages from TronLink](/tronlink-wallet-extension/receive-messages-from-tronlink)
  3. [Messages to Be Deprecated](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated)



# User accepts connection

**DEPRECATED** Message ID: `acceptWeb` This message is generated when:

  1. The user accepts connection. ![image](images/tronlink-wallet-extension_receive-messages-from-tronlink_messages-to-be-deprecated_user-accepts-connection_img_0.jpg)




Developers can get the connection acceptance message by listening to it:

Copy
    
    
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "acceptWeb") {
        // handler logic
        console.log('got acceptWeb event', e.data)
      }
    })

[PreviousUser disconnects from the website](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-disconnects-from-the-website)[NextUser requests to connect to the website](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-requests-to-connect-to-the-website)

Last updated 2 years ago
