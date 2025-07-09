  1. [TronLink App](/tronlink-app)
  2. [DeepLink](/tronlink-app/deeplink)



# Open DApp

### 

Use DeepLink to launch TronLink and open DApp in the DApp Explorer

Copy
    
    
    // Tronlink-v4.10.0
    // Link
    <a href='tronlinkoutside://pull.activity?param={}'>Open DApp</a>

Copy
    
    
    //  The parameter of param is the protocol data in json format
    //  Note: json.toString needs to be encoded with urlencode
    {
    	"url": "https://www.tronlink.org/", //target DApp
    	"action": "open",
    	"protocol": "tronlink",
    	"version": "1.0"
    }

[PreviousOpen Wallet](/tronlink-app/deeplink/open-wallet)[NextLogin by TronLink](/tronlink-app/deeplink/login-by-tronlink)

Last updated 2 years ago
