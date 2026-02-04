# Helios Ethereum RPC Call Analysis - Detailed Report

This report identifies all trigger points for Ethereum RPC calls in the Helios codebase.

## Summary of RPC Call Categories

The Helios codebase implements a trustless Ethereum light client that:
1. **Exposes RPC endpoints** via JSON-RPC server (core/src/jsonrpc/mod.rs)
2. **Implements client API** via HeliosApi trait (core/src/client/api.rs, node.rs)
3. **Makes upstream RPC calls** via execution providers (core/src/execution/providers/rpc.rs)
4. **Provides TypeScript bindings** (helios-ts/src/*.rs, lib.ts)
5. **Offers a Verifiable API** (verifiable-api/server/src/*.rs)

---

## Detailed RPC Trigger Points

| Filename | Line | RPC Method | Count |
|----------|------|------------|-------|
| core/src/jsonrpc/mod.rs | L68 | eth_getBalance | 1 |
| core/src/jsonrpc/mod.rs | L215 | eth_getBalance | 1 |
| core/src/client/api.rs | L24 | eth_getBalance | 1 |
| core/src/client/node.rs | L269 | eth_getBalance | 1 |
| helios-ts/src/ethereum.rs | L186 | eth_getBalance | 1 |
| helios-ts/src/ethereum.rs | L189 | eth_getBalance | 1 |
| helios-ts/src/opstack.rs | L126 | eth_getBalance | 1 |
| helios-ts/src/opstack.rs | L129 | eth_getBalance | 1 |
| helios-ts/src/linea.rs | L108 | eth_getBalance | 1 |
| helios-ts/src/linea.rs | L111 | eth_getBalance | 1 |
| helios-ts/lib.ts | L187 | eth_getBalance | 1 |
| helios-ts/lib.ts | L188 | eth_getBalance | 1 |
| examples/basic.rs | L54 | eth_getBalance | 1 |
| verifiable-api/server/src/handlers.rs | L128 | eth_getBalance | 1 |
| core/src/jsonrpc/mod.rs | L164 | eth_getStorageAt | 1 |
| core/src/jsonrpc/mod.rs | L416 | eth_getStorageAt | 1 |
| core/src/client/api.rs | L27 | eth_getStorageAt | 1 |
| core/src/client/node.rs | L306 | eth_getStorageAt | 1 |
| helios-ts/src/ethereum.rs | L293 | eth_getStorageAt | 1 |
| helios-ts/src/ethereum.rs | L302 | eth_getStorageAt | 1 |
| helios-ts/src/opstack.rs | L233 | eth_getStorageAt | 1 |
| helios-ts/src/opstack.rs | L242 | eth_getStorageAt | 1 |
| helios-ts/src/linea.rs | L215 | eth_getStorageAt | 1 |
| helios-ts/src/linea.rs | L224 | eth_getStorageAt | 1 |
| helios-ts/lib.ts | L214 | eth_getStorageAt | 1 |
| helios-ts/lib.ts | L215 | eth_getStorageAt | 1 |
| verifiable-api/server/src/handlers.rs | L128 | eth_getStorageAt | 1 |
| core/src/jsonrpc/mod.rs | L87 | eth_getCode | 1 |
| core/src/jsonrpc/mod.rs | L255 | eth_getCode | 1 |
| core/src/client/api.rs | L26 | eth_getCode | 1 |
| core/src/client/node.rs | L294 | eth_getCode | 1 |
| core/src/execution/providers/rpc.rs | L230 | eth_getCode | 1 |
| helios-ts/src/ethereum.rs | L285 | eth_getCode | 1 |
| helios-ts/src/ethereum.rs | L288 | eth_getCode | 1 |
| helios-ts/src/opstack.rs | L225 | eth_getCode | 1 |
| helios-ts/src/opstack.rs | L228 | eth_getCode | 1 |
| helios-ts/src/linea.rs | L207 | eth_getCode | 1 |
| helios-ts/src/linea.rs | L210 | eth_getCode | 1 |
| helios-ts/lib.ts | L211 | eth_getCode | 1 |
| helios-ts/lib.ts | L212 | eth_getCode | 1 |
| verifiable-api/server/src/handlers.rs | L128 | eth_getCode | 1 |
| verifiable-api/server/src/service.rs | L95 | eth_getCode | 1 |
| core/src/jsonrpc/mod.rs | L89 | eth_call | 1 |
| core/src/jsonrpc/mod.rs | L259 | eth_call | 1 |
| core/src/client/api.rs | L59 | eth_call | 1 |
| core/src/client/node.rs | L175 | eth_call | 1 |
| helios-ts/src/ethereum.rs | L326 | eth_call | 1 |
| helios-ts/src/ethereum.rs | L336 | eth_call | 1 |
| helios-ts/src/opstack.rs | L266 | eth_call | 1 |
| helios-ts/src/opstack.rs | L276 | eth_call | 1 |
| helios-ts/src/linea.rs | L248 | eth_call | 1 |
| helios-ts/src/linea.rs | L258 | eth_call | 1 |
| helios-ts/lib.ts | L220 | eth_call | 1 |
| helios-ts/lib.ts | L221 | eth_call | 1 |
| core/src/jsonrpc/mod.rs | L71 | eth_getTransactionCount | 1 |
| core/src/jsonrpc/mod.rs | L223 | eth_getTransactionCount | 1 |
| core/src/client/api.rs | L25 | eth_getTransactionCount | 1 |
| core/src/client/node.rs | L279 | eth_getTransactionCount | 1 |
| helios-ts/src/ethereum.rs | L235 | eth_getTransactionCount | 1 |
| helios-ts/src/ethereum.rs | L242 | eth_getTransactionCount | 1 |
| helios-ts/src/opstack.rs | L175 | eth_getTransactionCount | 1 |
| helios-ts/src/opstack.rs | L182 | eth_getTransactionCount | 1 |
| helios-ts/src/linea.rs | L157 | eth_getTransactionCount | 1 |
| helios-ts/src/linea.rs | L164 | eth_getTransactionCount | 1 |
| helios-ts/lib.ts | L200 | eth_getTransactionCount | 1 |
| helios-ts/lib.ts | L201 | eth_getTransactionCount | 1 |
| verifiable-api/server/src/handlers.rs | L127 | eth_getTransactionCount | 1 |
| core/src/jsonrpc/mod.rs | L77 | eth_getBlockTransactionCountByHash | 1 |
| core/src/jsonrpc/mod.rs | L231 | eth_getBlockTransactionCountByHash | 1 |
| helios-ts/src/ethereum.rs | L246 | eth_getBlockTransactionCountByHash | 1 |
| helios-ts/src/ethereum.rs | L251 | eth_getBlockTransactionCountByHash | 1 |
| helios-ts/src/opstack.rs | L186 | eth_getBlockTransactionCountByHash | 1 |
| helios-ts/src/opstack.rs | L191 | eth_getBlockTransactionCountByHash | 1 |
| helios-ts/src/linea.rs | L168 | eth_getBlockTransactionCountByHash | 1 |
| helios-ts/src/linea.rs | L173 | eth_getBlockTransactionCountByHash | 1 |
| helios-ts/lib.ts | L203 | eth_getBlockTransactionCountByHash | 1 |
| helios-ts/lib.ts | L204 | eth_getBlockTransactionCountByHash | 1 |
| core/src/jsonrpc/mod.rs | L82 | eth_getBlockTransactionCountByNumber | 1 |
| core/src/jsonrpc/mod.rs | L243 | eth_getBlockTransactionCountByNumber | 1 |
| helios-ts/src/ethereum.rs | L256 | eth_getBlockTransactionCountByNumber | 1 |
| helios-ts/src/ethereum.rs | L261 | eth_getBlockTransactionCountByNumber | 1 |
| helios-ts/src/opstack.rs | L196 | eth_getBlockTransactionCountByNumber | 1 |
| helios-ts/src/opstack.rs | L201 | eth_getBlockTransactionCountByNumber | 1 |
| helios-ts/src/linea.rs | L178 | eth_getBlockTransactionCountByNumber | 1 |
| helios-ts/src/linea.rs | L183 | eth_getBlockTransactionCountByNumber | 1 |
| helios-ts/lib.ts | L206 | eth_getBlockTransactionCountByNumber | 1 |
| helios-ts/lib.ts | L207 | eth_getBlockTransactionCountByNumber | 1 |
| core/src/jsonrpc/mod.rs | L126 | eth_getBlockByHash | 1 |
| core/src/jsonrpc/mod.rs | L324 | eth_getBlockByHash | 1 |
| core/src/client/api.rs | L42 | eth_getBlockByHash | 1 |
| core/src/client/node.rs | L461 | eth_getBlockByHash | 1 |
| helios-ts/src/ethereum.rs | L278 | eth_getBlockByHash | 1 |
| helios-ts/src/ethereum.rs | L280 | eth_getBlockByHash | 1 |
| helios-ts/src/opstack.rs | L218 | eth_getBlockByHash | 1 |
| helios-ts/src/opstack.rs | L220 | eth_getBlockByHash | 1 |
| helios-ts/src/linea.rs | L200 | eth_getBlockByHash | 1 |
| helios-ts/src/linea.rs | L202 | eth_getBlockByHash | 1 |
| helios-ts/lib.ts | L284 | eth_getBlockByHash | 1 |
| helios-ts/lib.ts | L285 | eth_getBlockByHash | 1 |
| verifiable-api/server/src/handlers.rs | L330 | eth_getBlockByHash | 1 |
| core/src/jsonrpc/mod.rs | L120 | eth_getBlockByNumber | 1 |
| core/src/jsonrpc/mod.rs | L316 | eth_getBlockByNumber | 1 |
| core/src/client/api.rs | L42 | eth_getBlockByNumber | 1 |
| core/src/client/node.rs | L461 | eth_getBlockByNumber | 1 |
| linea/src/consensus.rs | L122 | eth_getBlockByNumber | 1 |
| helios-ts/src/ethereum.rs | L267 | eth_getBlockByNumber | 1 |
| helios-ts/src/ethereum.rs | L273 | eth_getBlockByNumber | 1 |
| helios-ts/src/opstack.rs | L207 | eth_getBlockByNumber | 1 |
| helios-ts/src/opstack.rs | L213 | eth_getBlockByNumber | 1 |
| helios-ts/src/linea.rs | L189 | eth_getBlockByNumber | 1 |
| helios-ts/src/linea.rs | L195 | eth_getBlockByNumber | 1 |
| helios-ts/lib.ts | L280 | eth_getBlockByNumber | 1 |
| helios-ts/lib.ts | L281 | eth_getBlockByNumber | 1 |
| verifiable-api/server/src/handlers.rs | L330 | eth_getBlockByNumber | 1 |
| core/src/jsonrpc/mod.rs | L138 | eth_getTransactionByHash | 1 |
| core/src/jsonrpc/mod.rs | L350 | eth_getTransactionByHash | 1 |
| core/src/client/api.rs | L46 | eth_getTransactionByHash | 1 |
| core/src/client/node.rs | L360 | eth_getTransactionByHash | 1 |
| core/src/execution/providers/rpc.rs | L306 | eth_getTransactionByHash | 1 |
| helios-ts/src/ethereum.rs | L194 | eth_getTransactionByHash | 1 |
| helios-ts/src/ethereum.rs | L196 | eth_getTransactionByHash | 1 |
| helios-ts/src/opstack.rs | L134 | eth_getTransactionByHash | 1 |
| helios-ts/src/opstack.rs | L136 | eth_getTransactionByHash | 1 |
| helios-ts/src/linea.rs | L116 | eth_getTransactionByHash | 1 |
| helios-ts/src/linea.rs | L118 | eth_getTransactionByHash | 1 |
| helios-ts/lib.ts | L196 | eth_getTransactionByHash | 1 |
| helios-ts/lib.ts | L197 | eth_getTransactionByHash | 1 |
| verifiable-api/server/src/service.rs | L138 | eth_getTransactionByHash | 1 |
| core/src/jsonrpc/mod.rs | L140 | eth_getTransactionByBlockHashAndIndex | 1 |
| core/src/jsonrpc/mod.rs | L357 | eth_getTransactionByBlockHashAndIndex | 1 |
| core/src/client/api.rs | L47 | eth_getTransactionByBlockHashAndIndex | 1 |
| core/src/client/node.rs | L364 | eth_getTransactionByBlockHashAndIndex | 1 |
| helios-ts/src/ethereum.rs | L201 | eth_getTransactionByBlockHashAndIndex | 1 |
| helios-ts/src/ethereum.rs | L210 | eth_getTransactionByBlockHashAndIndex | 1 |
| helios-ts/src/opstack.rs | L141 | eth_getTransactionByBlockHashAndIndex | 1 |
| helios-ts/src/opstack.rs | L150 | eth_getTransactionByBlockHashAndIndex | 1 |
| helios-ts/src/linea.rs | L123 | eth_getTransactionByBlockHashAndIndex | 1 |
| helios-ts/src/linea.rs | L132 | eth_getTransactionByBlockHashAndIndex | 1 |
| helios-ts/lib.ts | L242 | eth_getTransactionByBlockHashAndIndex | 1 |
| helios-ts/lib.ts | L243 | eth_getTransactionByBlockHashAndIndex | 1 |
| verifiable-api/server/src/handlers.rs | L212 | eth_getTransactionByBlockHashAndIndex | 1 |
| verifiable-api/server/src/service.rs | L170 | eth_getTransactionByBlockHashAndIndex | 1 |
| core/src/jsonrpc/mod.rs | L146 | eth_getTransactionByBlockNumberAndIndex | 1 |
| core/src/jsonrpc/mod.rs | L369 | eth_getTransactionByBlockNumberAndIndex | 1 |
| core/src/client/api.rs | L47 | eth_getTransactionByBlockNumberAndIndex | 1 |
| core/src/client/node.rs | L364 | eth_getTransactionByBlockNumberAndIndex | 1 |
| helios-ts/src/ethereum.rs | L218 | eth_getTransactionByBlockNumberAndIndex | 1 |
| helios-ts/src/ethereum.rs | L225 | eth_getTransactionByBlockNumberAndIndex | 1 |
| helios-ts/src/opstack.rs | L158 | eth_getTransactionByBlockNumberAndIndex | 1 |
| helios-ts/src/opstack.rs | L165 | eth_getTransactionByBlockNumberAndIndex | 1 |
| helios-ts/src/linea.rs | L140 | eth_getTransactionByBlockNumberAndIndex | 1 |
| helios-ts/src/linea.rs | L147 | eth_getTransactionByBlockNumberAndIndex | 1 |
| helios-ts/lib.ts | L249 | eth_getTransactionByBlockNumberAndIndex | 1 |
| helios-ts/lib.ts | L250 | eth_getTransactionByBlockNumberAndIndex | 1 |
| verifiable-api/server/src/handlers.rs | L211 | eth_getTransactionByBlockNumberAndIndex | 1 |
| verifiable-api/server/src/service.rs | L175 | eth_getTransactionByBlockNumberAndIndex | 1 |
| core/src/jsonrpc/mod.rs | L134 | eth_getTransactionReceipt | 1 |
| core/src/jsonrpc/mod.rs | L336 | eth_getTransactionReceipt | 1 |
| core/src/client/api.rs | L53 | eth_getTransactionReceipt | 1 |
| core/src/client/node.rs | L348 | eth_getTransactionReceipt | 1 |
| core/src/execution/providers/rpc.rs | L345 | eth_getTransactionReceipt | 1 |
| helios-ts/src/ethereum.rs | L393 | eth_getTransactionReceipt | 1 |
| helios-ts/src/ethereum.rs | L395 | eth_getTransactionReceipt | 1 |
| helios-ts/src/opstack.rs | L333 | eth_getTransactionReceipt | 1 |
| helios-ts/src/opstack.rs | L335 | eth_getTransactionReceipt | 1 |
| helios-ts/src/linea.rs | L315 | eth_getTransactionReceipt | 1 |
| helios-ts/src/linea.rs | L317 | eth_getTransactionReceipt | 1 |
| helios-ts/lib.ts | L238 | eth_getTransactionReceipt | 1 |
| helios-ts/lib.ts | L239 | eth_getTransactionReceipt | 1 |
| verifiable-api/server/src/handlers.rs | L159 | eth_getTransactionReceipt | 1 |
| verifiable-api/server/src/handlers.rs | L165 | eth_getTransactionReceipt | 1 |
| verifiable-api/server/src/service.rs | L113 | eth_getTransactionReceipt | 1 |
| verifiable-api/server/src/service.rs | L117 | eth_getTransactionReceipt | 1 |
| verifiable-api/client/src/http.rs | L108 | eth_getTransactionReceipt | 1 |
| core/src/execution/providers/verifiable_api.rs | L254 | eth_getTransactionReceipt | 1 |
| core/src/jsonrpc/mod.rs | L152 | eth_getLogs | 1 |
| core/src/jsonrpc/mod.rs | L389 | eth_getLogs | 1 |
| core/src/client/api.rs | L78 | eth_getLogs | 1 |
| core/src/client/node.rs | L375 | eth_getLogs | 1 |
| core/src/client/node.rs | L386 | eth_getLogs | 1 |
| common/src/execution_provider.rs | L75 | eth_getLogs | 1 |
| core/src/execution/providers/rpc.rs | L392 | eth_getLogs | 1 |
| core/src/execution/providers/rpc.rs | L411 | eth_getLogs | 1 |
| helios-ts/src/ethereum.rs | L407 | eth_getLogs | 1 |
| helios-ts/src/ethereum.rs | L409 | eth_getLogs | 1 |
| helios-ts/src/opstack.rs | L347 | eth_getLogs | 1 |
| helios-ts/src/opstack.rs | L349 | eth_getLogs | 1 |
| helios-ts/src/linea.rs | L329 | eth_getLogs | 1 |
| helios-ts/src/linea.rs | L331 | eth_getLogs | 1 |
| helios-ts/lib.ts | L260 | eth_getLogs | 1 |
| helios-ts/lib.ts | L261 | eth_getLogs | 1 |
| verifiable-api/server/src/handlers.rs | L247 | eth_getLogs | 1 |
| verifiable-api/server/src/handlers.rs | L256 | eth_getLogs | 1 |
| verifiable-api/server/src/service.rs | L203 | eth_getLogs | 1 |
| verifiable-api/server/src/service.rs | L204 | eth_getLogs | 1 |
| verifiable-api/client/src/http.rs | L146 | eth_getLogs | 1 |
| core/src/execution/providers/verifiable_api.rs | L305 | eth_getLogs | 1 |
| core/src/execution/providers/verifiable_api.rs | L309 | eth_getLogs | 1 |
| core/src/jsonrpc/mod.rs | L156 | eth_getFilterLogs | 1 |
| core/src/jsonrpc/mod.rs | L400 | eth_getFilterLogs | 1 |
| core/src/client/api.rs | L81 | eth_getFilterLogs | 1 |
| core/src/client/node.rs | L384 | eth_getFilterLogs | 1 |
| helios-ts/src/ethereum.rs | L414 | eth_getFilterLogs | 1 |
| helios-ts/src/ethereum.rs | L416 | eth_getFilterLogs | 1 |
| helios-ts/src/opstack.rs | L354 | eth_getFilterLogs | 1 |
| helios-ts/src/opstack.rs | L356 | eth_getFilterLogs | 1 |
| helios-ts/src/linea.rs | L336 | eth_getFilterLogs | 1 |
| helios-ts/src/linea.rs | L338 | eth_getFilterLogs | 1 |
| helios-ts/lib.ts | L264 | eth_getFilterLogs | 1 |
| helios-ts/lib.ts | L265 | eth_getFilterLogs | 1 |
| core/src/jsonrpc/mod.rs | L154 | eth_getFilterChanges | 1 |
| core/src/jsonrpc/mod.rs | L393 | eth_getFilterChanges | 1 |

---

## Notes

1. **Excluded files**: Test files (tests/*.rs), benchmark files (benches/*.rs), mock files (mock_rpc.rs), and documentation files (*.md) were excluded per the requirements.

2. **Architecture**: Helios has a layered architecture where:
   - JSON-RPC server exposes the RPC interface
   - HeliosApi trait defines the internal API
   - Node implements the API by delegating to execution providers
   - Execution providers make actual upstream RPC calls

3. **Trigger point types**:
   - **Direct**: JSON-RPC method definition/implementation
   - **Indirect**: Client API methods that ultimately trigger RPC calls
   - **TypeScript bindings**: WASM bindings that expose RPC methods to JavaScript

4. **eth_getFilterChanges**: Note that the current implementation returns "not implemented" error (core/src/jsonrpc/mod.rs:397), but the method is still defined in the RPC interface.
