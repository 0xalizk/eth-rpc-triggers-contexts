# Wallet-POC Ethereum RPC Call Analysis - Detailed Report

This report documents all Ethereum RPC call trigger points found in the Wallet-POC codebase (Ambire Wallet), including the ambire-common submodule.

---

## eth_getCode (7 trigger points)

| File | Line | Context |
|------|------|---------|
| src/web/components/NetworkAvailableFeatures/NetworkAvailableFeatures.tsx | 63 | `provider.getCode(AMBIRE_ACCOUNT_FACTORY)` - Check if Ambire contracts are deployed on network |
| src/ambire-common/src/controllers/main/main.ts | 1084 | `provider.getCode(AMBIRE_ACCOUNT_FACTORY)` - Verify factory deployment status |
| src/ambire-common/src/libs/networks/networks.ts | 124 | `provider.getCode(SINGLETON)` - Check singleton contract deployment |
| src/ambire-common/src/libs/networks/networks.ts | 125 | `provider.getCode(AMBIRE_ACCOUNT_FACTORY)` - Check factory contract deployment |
| src/ambire-common/src/libs/networks/networks.ts | 161 | `provider.getCode(OPTIMISTIC_ORACLE)` - Check if network is optimistic rollup |
| src/ambire-common/src/libs/accountState/accountState.ts | 52 | `provider.getCode(addr)` - Check EOA account code (in batch) |
| src/ambire-common/src/libs/proxyDeploy/bytecode.ts | 14 | `provider.getCode(PROXY_AMBIRE_4337_ACCOUNT)` - Verify 4337 proxy deployment |

---

## eth_getTransactionReceipt (5 trigger points)

| File | Line | Context |
|------|------|---------|
| src/benzin/screens/BenzinScreen/hooks/useSteps/useSteps.ts | 274 | `provider.getTransactionReceipt(foundTxnId)` - Fetch receipt for transaction status tracking |
| src/web/extension-services/background/provider/ProviderController.ts | 504 | `provider.getTransactionReceipt(txnId)` - Single transaction receipt in wallet_getCallsStatus |
| src/web/extension-services/background/provider/ProviderController.ts | 515 | `provider.getTransactionReceipt(oneTxnId)` - Multiple transaction receipts in wallet_getCallsStatus |
| src/ambire-common/src/controllers/activity/activity.ts | 410 | `provider.getTransactionReceipt(txnId)` - Check transaction confirmation status |
| src/ambire-common/src/controllers/activity/activity.ts | 424 | `provider.getTransactionReceipt(frontRanTxnId)` - Handle front-run transaction detection |

---

## eth_getBlockByNumber (5 trigger points)

| File | Line | Context |
|------|------|---------|
| src/benzin/screens/BenzinScreen/hooks/useSteps/useSteps.ts | 418 | `provider.getBlock('latest', true)` - Get latest block for pending time calculation |
| src/benzin/screens/BenzinScreen/hooks/useSteps/useSteps.ts | 447 | `provider.getBlock(Number(txnReceipt.blockNumber))` - Get block data for confirmed transaction |
| src/legends/modules/character/screens/CharacterSelect/hooks/useMintCharacter/useMintCharacter.ts | 46 | `provider.getBlock(mintEvent.blockNumber)` - Get block timestamp for NFT mint event |
| src/ambire-common/src/libs/networks/networks.ts | 171 | `provider.getBlock('latest')` - Detect EIP-1559 fee support |
| src/ambire-common/src/libs/gasPrice/gasPrice.ts | 114 | `provider.getBlock(blockTag, true)` - Fetch block for gas price estimation |

---

## eth_call (5 trigger points)

| File | Line | Context |
|------|------|---------|
| src/benzin/screens/BenzinScreen/hooks/useSteps/useSteps.ts | 381 | `provider.call({...})` - Simulate failed transaction to extract revert reason |
| src/ambire-common/src/libs/deployless/deployless.ts | 117 | `provider.send('eth_call', [...])` - State override support detection |
| src/ambire-common/src/libs/deployless/deployless.ts | 159 | `provider.send('eth_call', [...])` - Deployless call with state override |
| src/ambire-common/src/libs/deployless/deployless.ts | 173 | `provider.call({...})` - Deployless call in proxy mode |
| src/ambire-common/src/libs/swapAndBridge/swapAndBridge.ts | 207 | `provider.call({...})` - Test approval call simulation |

---

## eth_getTransactionCount (4 trigger points)

| File | Line | Context |
|------|------|---------|
| src/ambire-common/src/controllers/main/main.ts | 2407 | `provider.getTransactionCount(senderAddr)` - Get nonce for raw transaction broadcast |
| src/ambire-common/src/libs/accountState/accountState.ts | 41 | `provider.getTransactionCount(addr)` - Get EOA nonces (in batch) |
| src/ambire-common/src/libs/estimate/estimateEOA.ts | 42 | `provider.getTransactionCount(account.addr)` - Get nonce for EOA gas estimation |
| src/ambire-common/src/libs/broadcast/broadcast.ts | 74 | `provider.getTransactionCount(from)` - Verify nonce before broadcast |

---

## eth_getTransactionByHash (2 trigger points)

| File | Line | Context |
|------|------|---------|
| src/benzin/screens/BenzinScreen/hooks/useSteps/useSteps.ts | 242 | `provider.getTransaction(foundTxnId)` - Fetch transaction data for status tracking |
| src/ambire-common/src/controllers/activity/activity.ts | 462 | `provider.getTransaction(txnId)` - Verify transaction exists when receipt unavailable |

---

## eth_getLogs (1 trigger point)

| File | Line | Context |
|------|------|---------|
| src/legends/modules/character/screens/CharacterSelect/hooks/useMintCharacter/useMintCharacter.ts | 42 | `provider.getLogs(filter)` - Query Transfer events for NFT minting verification |

---

## eth_getBalance (0 trigger points)

No direct calls found in source files. Method is defined in SAFE_RPC_METHODS for passthrough to RPC providers.

---

## eth_getStorageAt (0 trigger points)

No direct calls found. Method is defined in SAFE_RPC_METHODS for passthrough to RPC providers.

---

## eth_getBlockByHash (0 trigger points)

No direct calls found. Method is defined in SAFE_RPC_METHODS for passthrough to RPC providers.

---

## eth_getBlockTransactionCountByHash (0 trigger points)

No direct calls found. Method is defined in SAFE_RPC_METHODS for passthrough to RPC providers.

---

## eth_getBlockTransactionCountByNumber (0 trigger points)

No direct calls found. Method is defined in SAFE_RPC_METHODS for passthrough to RPC providers.

---

## eth_getTransactionByBlockHashAndIndex (0 trigger points)

No direct calls found. Method is defined in SAFE_RPC_METHODS for passthrough to RPC providers.

---

## eth_getTransactionByBlockNumberAndIndex (0 trigger points)

No direct calls found. Method is defined in SAFE_RPC_METHODS for passthrough to RPC providers.

---

## eth_getFilterLogs (0 trigger points)

No direct calls found. Method is defined in SAFE_RPC_METHODS for passthrough to RPC providers.

---

## eth_getFilterChanges (0 trigger points)

No direct calls found. Method is defined in SAFE_RPC_METHODS for passthrough to RPC providers.

---

## Notes

1. **Ethers.js Mapping**: Wallet-POC uses ethers.js (v6) which maps JavaScript methods to Ethereum JSON-RPC calls:
   - `provider.getLogs()` → `eth_getLogs`
   - `provider.getBlock()` → `eth_getBlockByNumber` (when called with number/tag)
   - `provider.getTransaction()` → `eth_getTransactionByHash`
   - `provider.getTransactionReceipt()` → `eth_getTransactionReceipt`
   - `provider.getCode()` → `eth_getCode`
   - `provider.getTransactionCount()` → `eth_getTransactionCount`
   - `provider.call()` → `eth_call`
   - `provider.send('eth_call', [...])` → `eth_call` (direct RPC)

2. **Wallet Extension Architecture**: This codebase is a browser extension wallet that primarily acts as a middleware/proxy for dApp RPC requests. Most RPC methods are defined in `SAFE_RPC_METHODS` (common.ts) and passed through to upstream providers.

3. **ambire-common Submodule**: The `src/ambire-common/` git submodule contains core wallet logic including:
   - Activity tracking (transaction status monitoring)
   - Account state management
   - Gas estimation
   - Network detection
   - Deployless contract calls (state override simulation)

4. **Deployless Pattern**: The `deployless.ts` library uses `eth_call` with state overrides to simulate contract deployments without actual on-chain deployment, enabling efficient account state queries.

5. **Test files excluded**: Test files (test/, *.test.ts) and compiled files (dist/) were excluded from this analysis.

6. **Key Components**:
   - **Benzin**: Transaction status tracking UI
   - **Legends**: NFT gaming platform
   - **ProviderController**: EIP-5792 implementation
   - **Activity Controller**: Transaction lifecycle management
   - **Networks Library**: Chain detection and configuration
   - **Deployless**: State override-based contract simulation
