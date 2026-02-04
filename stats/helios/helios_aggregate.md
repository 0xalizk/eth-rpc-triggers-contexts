# Helios Ethereum RPC Call Analysis - Aggregate Report

This report summarizes the total number of RPC call trigger points found in the Helios codebase, organized by RPC method.

| RPC Call | Aggregate Number of Calls |
|----------|---------------------------|
| eth_getLogsANY | 39 |
| eth_getTransactionReceipt | 20 |
| eth_getBlockByNumber | 15 |
| eth_getTransactionByHash | 15 |
| eth_getBalance | 14 |
| eth_getCode | 14 |
| eth_getTransactionCount | 14 |
| eth_getTransactionByBlockHashAndIndex | 14 |
| eth_getTransactionByBlockNumberAndIndex | 14 |
| eth_getStorageAt | 13 |
| eth_getBlockByHash | 13 |
| eth_call | 12 |
| eth_getBlockTransactionCountByHash | 10 |
| eth_getBlockTransactionCountByNumber | 10 |

---

## Summary

**Total RPC trigger points analyzed:** 217

### Top 5 Most Frequently Triggered RPC Methods:
1. **eth_getLogsANY** - 39 trigger points
2. **eth_getTransactionReceipt** - 20 trigger points
3. **eth_getBlockByNumber** / **eth_getTransactionByHash** - 15 trigger points each
4. **eth_getBalance** / **eth_getCode** / **eth_getTransactionCount** / **eth_getTransactionByBlockHashAndIndex** / **eth_getTransactionByBlockNumberAndIndex** - 14 trigger points each
5. **eth_getStorageAt** / **eth_getBlockByHash** - 13 trigger points each

### Coverage by Component:
- **Core JSON-RPC Server** (core/src/jsonrpc/): Method definitions and implementations
- **Client API** (core/src/client/): HeliosApi trait and Node implementation
- **Execution Providers** (core/src/execution/providers/): Actual RPC calls to upstream nodes
- **TypeScript Bindings** (helios-ts/): WASM bindings for browser/Node.js usage
- **Verifiable API** (verifiable-api/): REST API alternative to JSON-RPC

### Notes:
1. **eth_getLogsANY** is a pseudonym combining: eth_getLogs (25), eth_getFilterLogs (12), and eth_getFilterChanges (2)
2. `eth_getFilterChanges` is defined but not fully implemented (returns "not implemented" error)
3. The counts include both direct RPC endpoint definitions and indirect trigger points (method calls that eventually lead to RPC requests)
4. Test files, benchmark files, mock files, and documentation were excluded from the analysis
