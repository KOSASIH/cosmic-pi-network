import { DIDManager } from './did-manager';
import { Identity } from './identity';
import { Blockchain } from './blockchain';

const identity = new Identity({
  privateKey: 'privateKey',
  publicKey: 'publicKey',
});

const blockchain = new Blockchain({
  nodeUrl: 'https://example.com/blockchain',
});

const didManager = new DIDManager({
  identity,
  blockchain,
});

didManager.createDID('did:example:123').then(() => {
  console.log('DID created successfully!');
}).catch((error) => {
  console.error('Error creating DID:', error);
});
