
# User disconnects from the website

**DEPRECATED** Message ID: `disconnectWeb` This message is generated when:

  1. User actively disconnect from the website. ![image](images/tronlink-wallet-extension_receive-messages-from-tronlink_messages-to-be-deprecated_user-disconnects-from-the-website_img_0.jpg)




Developers can get the disconnection message by listening to it:

Copy
    
    
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "disconnectWeb") {
        // handler logic
        console.log('got disconnectWeb event', e.data)
      }
    })

[PreviousUser rejects connection](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-rejects-connection)[NextUser accepts connection](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-accepts-connection)

Last updated 2 years ago
