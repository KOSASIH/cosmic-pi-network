# DID Manager
============

This is a DID manager library that provides a simple way to create and resolve DIDs on a blockchain.

### Installation

```
1. npm install
```

### Usage

```
1. ts-node src/index.ts
```


### Configuration

You can configure the DID manager by creating a `.ctirc` file in the root of the project. The `.ctirc` file should contain the following configuration options:

```json
{
  "identity": {
    "privateKey": "privateKey",
    "publicKey": "publicKey"
  },
  "blockchain": {
    "nodeUrl": "https://example.com/blockchain"
  }
}
```

# License

This library is licensed under the MIT License.
