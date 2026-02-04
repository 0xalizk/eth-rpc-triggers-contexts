# Rotki Ethereum RPC Call Analysis - Aggregate Report

This report summarizes the total number of RPC call trigger points found in the Rotki codebase, organized by RPC method.

| RPC Call | Aggregate Number of Calls |
|----------|---------------------------|
| eth_getBlockByNumber | 3 |
| eth_getCode | 3 |
| eth_getTransactionByHash | 3 |
| eth_getTransactionCount | 3 |
| eth_call | 3 |
| eth_getLogsANY | 2 |
| eth_getTransactionReceipt | 2 |
| eth_getBalance | 2 |
| eth_getStorageAt | 0 |
| eth_getBlockByHash | 0 |
| eth_getBlockTransactionCountByHash | 0 |
| eth_getBlockTransactionCountByNumber | 0 |
| eth_getTransactionByBlockHashAndIndex | 0 |
| eth_getTransactionByBlockNumberAndIndex | 0 |

---

## Summary

**Total RPC trigger points analyzed:** 21

### Top 5 Most Frequently Triggered RPC Methods:
1. **eth_getBlockByNumber** / **eth_getCode** / **eth_getTransactionByHash** / **eth_getTransactionCount** / **eth_call** - 3 trigger points each
2. **eth_getLogsANY** / **eth_getTransactionReceipt** / **eth_getBalance** - 2 trigger points each

### RPC Methods Not Used:
- eth_getStorageAt
- eth_getBlockByHash
- eth_getBlockTransactionCountByHash
- eth_getBlockTransactionCountByNumber
- eth_getTransactionByBlockHashAndIndex
- eth_getTransactionByBlockNumberAndIndex

### Coverage by Component:
- **EVM Node Inquirer** (rotkehlchen/chain/evm/node_inquirer.py): Primary RPC implementation with web3.py
- **Avalanche Manager** (rotkehlchen/chain/avalanche/manager.py): Chain-specific RPC calls for Avalanche
- **Indexer Fallback** (rotkehlchen/externalapis/etherscan_like.py): Etherscan/Blockscout/Routescan fallback layer
- **Active Management** (rotkehlchen/chain/evm/active_management/manager.py): Transaction building utilities
- **RPC Nodes Mixin** (rotkehlchen/chain/mixins/rpc_nodes.py): Node capability detection
- **Aggregator** (rotkehlchen/chain/aggregator.py): Multi-chain balance aggregation

### Architecture Notes:
1. **eth_getLogsANY** is a pseudonym combining: eth_getLogs (2), eth_getFilterLogs (0), and eth_getFilterChanges (0)
2. Rotki uses web3.py as its primary Ethereum RPC client library
3. All EVM chains share the common `node_inquirer.py` implementation
4. Indexer APIs (Etherscan-like) serve as fallbacks when RPC nodes are unavailable
5. The codebase favors `eth_getBlockByNumber` over `eth_getBlockByHash`
6. Filter-based log retrieval is not used; `eth_getLogs` is called directly
7. Test files, benchmark files, mock files, and documentation were excluded from the analysis
