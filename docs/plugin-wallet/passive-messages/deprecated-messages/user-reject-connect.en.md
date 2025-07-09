# User rejects connection

**DEPRECATED** 

Message ID: `rejectWeb` 

This message is generated when:

  1. The DApp requests a connection and the user rejects the connection in the pop-up window. ![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252FVn5c8NKJSvDRJlKqHpVd%252Frejected-connect.jpg%3Falt%3Dmedia%26token%3Daf5565dc-c798-4f58-a317-a3dc0ed91c59&width=300&dpr=4&quality=100&sign=ad111b4b&sv=2)




Developers can get the connection rejection message by listening to it:

```shell
    
    
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "rejectWeb") {
        // handler logic
        console.log('got rejectWeb event', e.data)
      }
    })
```