# Rotki Ethereum RPC Call Analysis - Detailed Report

This report documents all Ethereum RPC call trigger points found in the Rotki codebase.

---

## eth_getLogs (2 trigger points)

| File | Line | Context |
|------|------|---------|
| rotkehlchen/chain/evm/node_inquirer.py | 135 | `web3.eth.get_logs(filter_args)` - Direct web3.py call in contract event querying |
| rotkehlchen/externalapis/etherscan_like.py | 882 | `action='getLogs'` - Indexer fallback via Etherscan-like API |

---

## eth_getTransactionReceipt (2 trigger points)

| File | Line | Context |
|------|------|---------|
| rotkehlchen/chain/evm/node_inquirer.py | 773 | `web3.eth.get_transaction_receipt(tx_hash)` - Direct web3.py call for receipt retrieval |
| rotkehlchen/externalapis/etherscan_like.py | 836 | `method='eth_getTransactionReceipt'` - Indexer fallback via RPC proxy |

---

## eth_getBalance (2 trigger points)

| File | Line | Context |
|------|------|---------|
| rotkehlchen/chain/evm/node_inquirer.py | 302 | `node_web3.eth.get_balance(account=address, block_identifier=block_identifier)` - Historical balance queries |
| rotkehlchen/chain/avalanche/manager.py | 54 | `self.w3.eth.get_balance(account)` - Avalanche-specific AVAX balance query |

---

## eth_getBlockByNumber (3 trigger points)

| File | Line | Context |
|------|------|---------|
| rotkehlchen/chain/evm/node_inquirer.py | 598 | `web3.eth.get_block(num)` - Block data retrieval by number |
| rotkehlchen/chain/avalanche/manager.py | 63 | `self.w3.eth.get_block(num)` - Avalanche-specific block retrieval |
| rotkehlchen/externalapis/etherscan_like.py | 793 | `method='eth_getBlockByNumber'` - Indexer fallback via RPC proxy |

---

## eth_getCode (3 trigger points)

| File | Line | Context |
|------|------|---------|
| rotkehlchen/chain/evm/node_inquirer.py | 626 | `web3.eth.get_code(account)` - Contract bytecode retrieval |
| rotkehlchen/chain/avalanche/manager.py | 69 | `self.w3.eth.get_code(account)` - Avalanche-specific bytecode retrieval |
| rotkehlchen/externalapis/etherscan_like.py | 822 | `method='eth_getCode'` - Indexer fallback via RPC proxy |

---

## eth_getTransactionByHash (3 trigger points)

| File | Line | Context |
|------|------|---------|
| rotkehlchen/chain/evm/node_inquirer.py | 826 | `web3.eth.get_transaction(tx_hash)` - Transaction data retrieval by hash |
| rotkehlchen/chain/mixins/rpc_nodes.py | 210 | `web3.eth.get_transaction(self._get_pruned_check_tx_hash())` - Node pruning status check |
| rotkehlchen/externalapis/etherscan_like.py | 812 | `method='eth_getTransactionByHash'` - Indexer fallback via RPC proxy |

---

## eth_getTransactionCount (3 trigger points)

| File | Line | Context |
|------|------|---------|
| rotkehlchen/chain/aggregator.py | 1029 | `avax_manager.w3.eth.get_transaction_count(address)` - Avalanche activity detection |
| rotkehlchen/chain/evm/active_management/manager.py | 41 | `rpc_client.eth.get_transaction_count(from_address)` - Token transfer nonce retrieval |
| rotkehlchen/chain/evm/active_management/manager.py | 85 | `rpc_client.eth.get_transaction_count(from_address)` - Native token transfer nonce retrieval |

---

## eth_call (3 trigger points)

| File | Line | Context |
|------|------|---------|
| rotkehlchen/chain/evm/node_inquirer.py | 712 | `contract.caller(block_identifier=block_identifier)` - Contract method call via web3.py |
| rotkehlchen/chain/avalanche/manager.py | 86 | `contract.caller` method invocation - Avalanche-specific contract calls |
| rotkehlchen/externalapis/etherscan_like.py | 851 | `method='eth_call'` - Indexer fallback via RPC proxy |

---

## eth_getStorageAt (0 trigger points)

No direct calls found in the codebase.

---

## eth_getBlockByHash (0 trigger points)

No direct calls found. Rotki uses block number-based queries instead.

---

## eth_getBlockTransactionCountByHash (0 trigger points)

No direct calls found in the codebase.

---

## eth_getBlockTransactionCountByNumber (0 trigger points)

No direct calls found in the codebase.

---

## eth_getTransactionByBlockHashAndIndex (0 trigger points)

No direct calls found in the codebase.

---

## eth_getTransactionByBlockNumberAndIndex (0 trigger points)

No direct calls found in the codebase.

---

## eth_getFilterLogs (0 trigger points)

No direct calls found. Rotki uses `eth_getLogs` directly instead of filter-based approaches.

---

## eth_getFilterChanges (0 trigger points)

No direct calls found. Rotki uses `eth_getLogs` directly instead of filter-based approaches.

---

## Notes

1. **Web3.py Mapping**: Rotki uses web3.py library which maps Python methods to Ethereum JSON-RPC calls:
   - `web3.eth.get_balance()` → `eth_getBalance`
   - `web3.eth.get_logs()` → `eth_getLogs`
   - `web3.eth.get_block()` → `eth_getBlockByNumber` (when called with number)
   - `web3.eth.get_transaction()` → `eth_getTransactionByHash`
   - `web3.eth.get_transaction_receipt()` → `eth_getTransactionReceipt`
   - `web3.eth.get_code()` → `eth_getCode`
   - `web3.eth.get_transaction_count()` → `eth_getTransactionCount`
   - `contract.caller.*` → `eth_call`

2. **Dual-Layer Architecture**: Rotki has a fallback system:
   - Primary: Direct RPC node calls via web3.py
   - Fallback: Indexer APIs (Etherscan, Blockscout, Routescan) that proxy RPC calls

3. **Avalanche-Specific**: Some RPC methods have dedicated implementations in the Avalanche manager for chain-specific handling.

4. **Test files, mock files, and documentation were excluded from this analysis.**
