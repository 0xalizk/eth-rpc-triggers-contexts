# Wallet-POC Ethereum RPC Call Analysis - Aggregate Report

This report summarizes the total number of RPC call trigger points found in the Wallet-POC codebase (Ambire Wallet), including the ambire-common submodule, organized by RPC method.

| RPC Call | Aggregate Number of Calls |
|----------|---------------------------|
| eth_getCode | 7 |
| eth_getTransactionReceipt | 5 |
| eth_getBlockByNumber | 5 |
| eth_call | 5 |
| eth_getTransactionCount | 4 |
| eth_getTransactionByHash | 2 |
| eth_getLogsANY | 1 |
| eth_getBalance | 0 |
| eth_getStorageAt | 0 |
| eth_getBlockByHash | 0 |
| eth_getBlockTransactionCountByHash | 0 |
| eth_getBlockTransactionCountByNumber | 0 |
| eth_getTransactionByBlockHashAndIndex | 0 |
| eth_getTransactionByBlockNumberAndIndex | 0 |

---

## Summary

**Total RPC trigger points analyzed:** 29

### Top RPC Methods by Frequency:
1. **eth_getCode** - 7 trigger points
2. **eth_getTransactionReceipt** / **eth_getBlockByNumber** / **eth_call** - 5 trigger points each
3. **eth_getTransactionCount** - 4 trigger points
4. **eth_getTransactionByHash** - 2 trigger points
5. **eth_getLogsANY** - 1 trigger point

### RPC Methods Not Used (Direct Calls):
- eth_getBalance
- eth_getStorageAt
- eth_getBlockByHash
- eth_getBlockTransactionCountByHash
- eth_getBlockTransactionCountByNumber
- eth_getTransactionByBlockHashAndIndex
- eth_getTransactionByBlockNumberAndIndex

### Coverage by Component:

**wallet-poc (main codebase):** 10 trigger points
- **Benzin Screen** (src/benzin/): Transaction status tracking - 5 trigger points
- **Legends NFT** (src/legends/): NFT minting verification - 2 trigger points
- **Provider Controller** (src/web/extension-services/): EIP-5792 implementation - 2 trigger points
- **Network Features** (src/web/components/): Contract deployment check - 1 trigger point

**ambire-common (submodule):** 19 trigger points
- **Activity Controller**: Transaction lifecycle management - 3 trigger points
- **Networks Library**: Chain detection and configuration - 4 trigger points
- **Account State**: EOA state queries - 2 trigger points
- **Deployless Library**: State override simulation - 3 trigger points
- **Main Controller**: Core wallet operations - 2 trigger points
- **Estimate/Broadcast**: Transaction preparation - 3 trigger points
- **Swap & Bridge**: Token approval simulation - 1 trigger point
- **Proxy Deploy**: 4337 account deployment - 1 trigger point

### Architecture Notes:
1. **eth_getLogsANY** is a pseudonym combining: eth_getLogs (1), eth_getFilterLogs (0), and eth_getFilterChanges (0)
2. Wallet-POC is a **browser extension wallet** that primarily proxies RPC requests to upstream providers
3. **eth_getCode** is heavily used for contract deployment verification (7 calls) - detecting whether Ambire contracts are deployed on various networks
4. The **Deployless pattern** uses `eth_call` with state overrides for efficient account state simulation
5. Uses ethers.js v6 as the primary Ethereum library
6. Test files, benchmark files, mock files, and documentation were excluded from the analysis
