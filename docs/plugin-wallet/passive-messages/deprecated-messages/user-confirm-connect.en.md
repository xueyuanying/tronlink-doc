# User accepts connection

**DEPRECATED** 

Message ID: `acceptWeb` 
This message is generated when:

  1. The user accepts connection. ![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252Fe2Xpt54odMG1NNDrbCVV%252Fapproved-connect.jpg%3Falt%3Dmedia%26token%3D72a4f125-8a42-4b60-b675-cf25d3bb6dc1&width=300&dpr=4&quality=100&sign=d0ff6797&sv=2)




Developers can get the connection acceptance message by listening to it:

Copy
    
    
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "acceptWeb") {
        // handler logic
        console.log('got acceptWeb event', e.data)
      }
    })

[PreviousUser disconnects from the website](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-disconnects-from-the-website)[NextUser requests to connect to the website](/tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-requests-to-connect-to-the-website)