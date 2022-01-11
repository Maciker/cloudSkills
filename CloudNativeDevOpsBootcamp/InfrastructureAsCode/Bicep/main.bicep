param name string = 'uniquestoragename12345678'
param location string = 'eastus'

var storageSku =  'Standard_LRS'

resource storegeaccount 'Microsoft.Storage/storageAccounts@2020-08-01-preview' = {
  name: name
  location: location
  kind: 'Storage'
  sku: {
    name: storageSku
  }
  properties: {
    allowBlobPublicAccess: false
  }
}

output id string = storegeaccount.id
