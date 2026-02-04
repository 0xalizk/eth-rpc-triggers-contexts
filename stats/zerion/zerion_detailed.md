# Zerion RPC Calls - Detailed Analysis

**Note:** The zerion directory contains scraped website content from app.zerion.io, not a source code repository. The only analyzable file is a minified JavaScript bundle (`index-iYNkx94u.js`). Line numbers refer to this minified file where RPC method definitions/calls appear.

## RPC Calls Found

| Filename | RPC Call | Count |
|----------|----------|-------|
| app.zerion.io/assets/index-iYNkx94u.js L192 | eth_call | 2 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_call | 3 |
| app.zerion.io/assets/index-iYNkx94u.js L192 | eth_getTransactionReceipt | 2 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getTransactionReceipt | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L1347 | eth_getTransactionReceipt | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L192 | eth_getBlockByNumber | 2 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getBlockByNumber | 2 |
| app.zerion.io/assets/index-iYNkx94u.js L192 | eth_getTransactionByHash | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getTransactionByHash | 2 |
| app.zerion.io/assets/index-iYNkx94u.js L192 | eth_getLogs | 2 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getLogs | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L192 | eth_getTransactionCount | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getTransactionCount | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L192 | eth_getCode | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getCode | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getBalance | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getStorageAt | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getBlockByHash | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getBlockTransactionCountByHash | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getBlockTransactionCountByNumber | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getTransactionByBlockHashAndIndex | 1 |
| app.zerion.io/assets/index-iYNkx94u.js L195 | eth_getTransactionByBlockNumberAndIndex | 1 |

## Summary by RPC Method

| RPC Call | Total Occurrences |
|----------|-------------------|
| eth_call | 5 |
| eth_getTransactionReceipt | 4 |
| eth_getBlockByNumber | 4 |
| eth_getTransactionByHash | 3 |
| eth_getLogs | 3 |
| eth_getTransactionCount | 2 |
| eth_getCode | 2 |
| eth_getBalance | 1 |
| eth_getStorageAt | 1 |
| eth_getBlockByHash | 1 |
| eth_getBlockTransactionCountByHash | 1 |
| eth_getBlockTransactionCountByNumber | 1 |
| eth_getTransactionByBlockHashAndIndex | 1 |
| eth_getTransactionByBlockNumberAndIndex | 1 |
| eth_getFilterLogs | 0 |
| eth_getFilterChanges | 0 |

## Notes

- The JavaScript file is minified/bundled, making precise call-site analysis difficult
- Most RPC methods appear as part of a web3.js or similar library bundled into the application
- Line 192 and 195 contain the bulk of the web3 method definitions
- Line 1347 contains application-specific code intercepting `eth_getTransactionReceipt` for local action handling
