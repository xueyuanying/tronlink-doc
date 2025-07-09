  1. [TronLink App](/tronlink-app)
  2. [DeepLink](/tronlink-app/deeplink)



# Open Wallet

### 

Launch TronLink wallet via DeepLink

Copy
    
    
    // Tronlink-v4.10.0
    // Link
    <a href='tronlinkoutside://pull.activity?param={}'>Open Tronlink</a>

Copy
    
    
    // The parameter of param is the protocol data in json format
    // Note: json.toString needs to be encoded with urlencode
    {
    	"action": "open",
    	"protocol": "tronlink",
    	"version": "1.0"
    }

[PreviousDeepLink](/tronlink-app/deeplink)[NextOpen DApp](/tronlink-app/deeplink/open-dapp)

Last updated 2 years ago
