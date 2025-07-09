# User requests to connect to the website

**DEPRECATED** Message ID: `connectWeb` This message is generated when:

  1. The user requests to connect to the website. ![](https://docs.tronlink.org/~gitbook/image?url=https%3A%2F%2F1639117838-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FDolSJpJ5tqTIRP95VixZ%252Fuploads%252FkgjbJqJyN28pHhagnn6i%252Fconnect-website-initiative.jpg%3Falt%3Dmedia%26token%3Db6edd382-8eae-4682-8ba7-a50153fd441c&width=300&dpr=4&quality=100&sign=b1384310&sv=2)




Developers can get the connection request message by listening to it:

```shell
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action == "connectWeb") {
        // handler logic
        console.log('got connectWeb event', e.data)
      }
    })
```
