interface BlockchainOptions {
  nodeUrl: string;
}

class Blockchain {
  private nodeUrl: string;

  constructor(options: BlockchainOptions) {
    this.nodeUrl = options.nodeUrl;
  }

  async createDID(did: string): Promise<void> {
    // Create a new DID on the blockchain
    const response = await fetch(`${this.nodeUrl}/createDID`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ did }),
    });
    if (!response.ok) {
      throw new Error(`Error creating DID: ${response.statusText}`);
    }
  }

  async resolveDID(did: string): Promise<string> {
    // Resolve a DID on the blockchain
    const response = await fetch(`${this.nodeUrl}/resolveDID`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ did }),
    });
    if (!response.ok) {
      throw new Error(`Error resolving DID: ${response.statusText}`);
    }
    return await response.json();
  }
}

export { Blockchain };
