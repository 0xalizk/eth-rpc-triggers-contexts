# Aave Frontend - Aggregate Ethereum RPC Call Statistics

| RPC Call | Aggregate Count |
|----------|-----------------|
| eth_getTransactionReceipt | 33 |
| eth_call | 5 |
| eth_getCode | 3 |
| eth_getBlockByNumber | 1 |
| eth_getBlockByHash | 1 |
| eth_getTransactionByHash | 1 |
| eth_getBalance | 1 |
| eth_getLogsANY | 0 |

**Total RPC Trigger Points: 45**

---

## Summary

The Aave frontend makes heavy use of `eth_getTransactionReceipt` (33 calls) primarily through the `.wait(1)` pattern after submitting transactions. This is used to confirm that transactions have been mined before updating the UI state.

The `eth_call` RPC method (5 calls) is used for:
- Reading contract state (balanceOf, multicall operations)
- Error inspection after failed transactions

`eth_getCode` (3 calls) is used for:
- Detecting if an address is a smart contract wallet
- Identifying Safe wallets specifically

Other RPC calls (`eth_getBlockByNumber`, `eth_getBlockByHash`, `eth_getTransactionByHash`, `eth_getBalance`) are used sparingly for specific features like finality estimation, transaction error retrieval, and native token balance fetching.

**Note:** Many contract interactions (supply, borrow, repay, withdraw, stake, etc.) go through the `@aave/contract-helpers` library which internally uses `eth_call` for data fetching. These are not explicitly counted as individual trigger points since they're abstracted behind service layer calls.
