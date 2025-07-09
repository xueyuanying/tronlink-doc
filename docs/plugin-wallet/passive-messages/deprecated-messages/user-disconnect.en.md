# User disconnects from the website

**DEPRECATED** 

Message ID: `disconnectWeb` 
This message is generated when:

  1. User actively disconnect from the website. ![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252FlDR8RaRejklpP9jDTlnG%252Fdisconnect-website.jpg%3Falt%3Dmedia%26token%3D9c18af16-0b57-4eb7-8028-39eaf55e44c3&width=300&dpr=4&quality=100&sign=1347bd73&sv=2)




Developers can get the disconnection message by listening to it:

```shell
    
    
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "disconnectWeb") {
        // handler logic
        console.log('got disconnectWeb event', e.data)
      }
    })
```