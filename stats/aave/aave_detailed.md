# Aave Frontend - Detailed Ethereum RPC Calls

This document lists all Ethereum RPC call trigger points found in the Aave interface codebase.

| Filename | RPC Call | Count |
|----------|----------|-------|
| src/helpers/useTransactionHandler.tsx L119 | eth_getTransactionReceipt | 1 |
| src/hooks/useApprovalTx.tsx L134 | eth_getTransactionReceipt | 1 |
| src/hooks/useApprovalTx.tsx L187 | eth_getTransactionReceipt | 1 |
| src/helpers/useParaSwapTransactionHandler.tsx L121 | eth_getTransactionReceipt | 1 |
| src/helpers/useGovernanceDelegate.tsx L85 | eth_getTransactionReceipt | 1 |
| src/hooks/useSwapOrdersTracking.tsx L264 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Supply/SupplyActions.tsx L168 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Supply/SupplyActions.tsx L178 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Supply/SupplyWrappedTokenActions.tsx L155 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Supply/SupplyWrappedTokenActions.tsx L166 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Borrow/BorrowActions.tsx L88 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Borrow/BorrowActions.tsx L117 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Repay/RepayActions.tsx L174 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Repay/RepayActions.tsx L198 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Withdraw/WithdrawAndUnwrapActions.tsx L137 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Withdraw/WithdrawAndUnwrapActions.tsx L146 | eth_getTransactionReceipt | 1 |
| src/components/transactions/SavingsGho/SavingsGhoWithdrawActions.tsx L90 | eth_getTransactionReceipt | 1 |
| src/components/transactions/SavingsGho/SavingsGhoWithdrawActions.tsx L109 | eth_getTransactionReceipt | 1 |
| src/components/transactions/GovVote/GovVoteActions.tsx L288 | eth_getTransactionReceipt | 1 |
| src/components/transactions/GovRepresentatives/GovRepresentativesActions.tsx L46 | eth_getTransactionReceipt | 1 |
| src/components/transactions/StakingMigrate/StakingMigrateActions.tsx L143 | eth_getTransactionReceipt | 1 |
| src/components/transactions/CancelCowOrder/CancelAdapterOrderActions.tsx L78 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Swap/actions/approval/useSwapTokenApproval.ts L291 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Swap/actions/approval/useSwapTokenApproval.ts L414 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Swap/actions/DebtSwap/DebtSwapActionsViaParaswap.tsx L146 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Swap/actions/RepayWithCollateral/RepayWithCollateralActionsViaParaswap.tsx L203 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Swap/actions/SwapActions/SwapActionsViaParaswap.tsx L98 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Swap/actions/CollateralSwap/CollateralSwapActionsViaParaswapAdapters.tsx L166 | eth_getTransactionReceipt | 1 |
| src/components/transactions/Swap/actions/WithdrawAndSwap/WithdrawAndSwapActionsViaParaswap.tsx L115 | eth_getTransactionReceipt | 1 |
| src/modules/umbrella/UnstakeModalActions.tsx L162 | eth_getTransactionReceipt | 1 |
| src/modules/umbrella/UmbrellaActions.tsx L186 | eth_getTransactionReceipt | 1 |
| src/modules/umbrella/UmbrellaClaimActions.tsx L85 | eth_getTransactionReceipt | 1 |
| src/modules/umbrella/StakeCooldownActions.tsx L52 | eth_getTransactionReceipt | 1 |
| src/helpers/provider.ts L4 | eth_getCode | 1 |
| src/helpers/provider.ts L24 | eth_getCode | 1 |
| src/hooks/useIsContractAddress.ts L12 | eth_getCode | 1 |
| src/libs/web3-data-provider/Web3Provider.tsx L137 | eth_getTransactionByHash | 1 |
| src/libs/web3-data-provider/Web3Provider.tsx L139 | eth_call | 1 |
| src/services/GovernanceV3Service.ts L100 | eth_getBlockByHash | 1 |
| src/components/transactions/Bridge/useGetFinalityTime.tsx L16 | eth_getBlockByNumber | 1 |
| src/hooks/generic/useTokensBalance.ts L48 | eth_call | 1 |
| src/hooks/generic/useTokensBalance.ts L60 | eth_getBalance | 1 |
| src/hooks/generic/useTokensBalance.ts L61 | eth_call | 1 |
| src/services/Erc20Service.ts L22 | eth_call | 1 |
| src/components/transactions/Swap/inputs/primitives/SwapAssetInput.tsx L231 | eth_call | 1 |

**Notes:**
- All `.wait(1)` calls trigger `eth_getTransactionReceipt` RPC calls (they poll until confirmation)
- `provider.getCode()` maps to `eth_getCode`
- `provider.getBalance()` maps to `eth_getBalance`
- `provider.getTransaction()` maps to `eth_getTransactionByHash`
- `provider.getBlock()` maps to `eth_getBlockByHash` or `eth_getBlockByNumber`
- `provider.call()` and contract read calls (like `balanceOf`) map to `eth_call`
- `multicall.call()` batches multiple `eth_call` invocations into a single RPC call
- `provider.getTransactionReceipt()` maps to `eth_getTransactionReceipt`
