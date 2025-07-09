  1. [TronLink Wallet Extension](/tronlink-wallet-extension)
  2. [Receive messages from TronLink](/tronlink-wallet-extension/receive-messages-from-tronlink)



# Account Change Message

Message ID: `accountsChanged`

**Overview**

This message is generated when:

  1. Users log in

  2. Users switch accounts

  3. Users lock accounts

  4. The wallet is automatically locked after timeout




**Specification**

**Example**

Copy
    
    
    window.addEventListener('message', function (e) {
      if (e.data.message && e.data.message.action === "accountsChanged") {
        // handler logic
        console.log('got accountsChanged event', e.data)
      }
    })

**Returns**

Copy
    
    
    interface MessageEventAccountsChangedData {
      isTronLink: boolean;
      message: {
        action: string;
        data: {
          address: string | boolean;
        }
      }
    }

**Return value example**

  1. When users log in, the content of the message body is:




Copy
    
    
    {
      "data": {
        "address": "TZ5XixnRyraxJJy996Q1sip85PHWuj4793" // Last selected account address
      }
    }

  1. When users switch accounts, the content of the message body is:




Copy
    
    
    {
      "data": {
        "address": "TRKb2nAnCBfwxnLxgoKJro6VbyA6QmsuXq" // Newly selected account address
      }
    }

  1. When users lock accounts and the wallet is automatically locked due to timeout, the message body content is:




Copy
    
    
    {
      "data": {
        "address": false
      }
    }

[PreviousReceive messages from TronLink](/tronlink-wallet-extension/receive-messages-from-tronlink)[NextNetwork Change Message](/tronlink-wallet-extension/receive-messages-from-tronlink/network-change-message)

Last updated 2 years ago
