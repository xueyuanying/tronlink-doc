  1. [TronLink Wallet Extension](/tronlink-wallet-extension)
  2. [Receive messages from TronLink](/tronlink-wallet-extension/receive-messages-from-tronlink)
  3. [Messages to Be Deprecated](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated)



# User rejects connection

**DEPRECATED** Message ID: `rejectWeb` This message is generated when:

  1. The DApp requests a connection and the user rejects the connection in the pop-up window. ![image](images/tronlink-wallet-extension_receive-messages-from-tronlink_messages-to-be-deprecated_user-rejects-connection_img_0.jpg)




Developers can get the connection rejection message by listening to it:

Copy
    
    
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "rejectWeb") {
        // handler logic
        console.log('got rejectWeb event', e.data)
      }
    })

[PreviousMessages to Be Deprecated](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated)[NextUser disconnects from the website](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-disconnects-from-the-website)

Last updated 2 years ago
