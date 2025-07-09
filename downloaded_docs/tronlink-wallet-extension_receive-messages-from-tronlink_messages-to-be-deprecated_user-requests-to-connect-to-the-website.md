  1. [TronLink Wallet Extension](/tronlink-wallet-extension)
  2. [Receive messages from TronLink](/tronlink-wallet-extension/receive-messages-from-tronlink)
  3. [Messages to Be Deprecated](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated)



# User requests to connect to the website

**DEPRECATED** Message ID: `connectWeb` This message is generated when:

  1. The user requests to connect to the website. ![image](images/tronlink-wallet-extension_receive-messages-from-tronlink_messages-to-be-deprecated_user-requests-to-connect-to-the-website_img_0.jpg)




Developers can get the connection request message by listening to it:

Copy
    
    
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "connectWeb") {
        // handler logic
        console.log('got connectWeb event', e.data)
      }
    })

[PreviousUser accepts connection](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-accepts-connection)[NextStart Developing](/dapp/start-developing)

Last updated 2 years ago
