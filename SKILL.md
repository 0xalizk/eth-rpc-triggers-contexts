---
name: scrape-rpc-calls
description: Crawl the codebase and find all Ethereum RPC calls. Use it when asked to scrape Ethereum RPC calls.
---

Find all points in the codebase where an Ethereum RPC call is triggered. Start by analyzing the codebase to find where the concrete implementation of each rpc call is located in the codebase. Then, analyze the codebase to identify all rpc trigger points. A trigger point can be a direct call to the method implementing the rpc call, or an indirect call where a line of code triggers one or more intermediary calls that ultimately lead to the concrete rpc call. 

When searching for points in the codebase where an Ethereum RPC call is triggered, whether directly or indirectly, please follow these rules: 

1. Your source of truth for Ethereum RPC specificication is this page: https://ethereum.org/developers/docs/apis/json-rpc
2. Only consider the following RPC calls, ignore all others:
  - eth_getBalance
  - eth_getStorageAt
  - eth_getCode
  - eth_call
  - eth_getTransactionCount
  - eth_getBlockTransactionCountByHash
  - eth_getBlockTransactionCountByNumber
  - eth_getBlockByHash
  - eth_getBlockByNumber
  - eth_getTransactionByHash
  - eth_getTransactionByBlockHashAndIndex
  - eth_getTransactionByBlockNumberAndIndex
  - eth_getTransactionReceipt
  - eth_getLogs
  - eth_getFilterLogs
  - eth_getFilterChanges
3. Ignore RPC calls made in a test context like test files or mock files. If you are unsure if it is a testing or mocking context, assume it is NOT by default
4. Ignore RPC calls in a documentation context like markdown files or code comments
5. Tally and tabulate the RPC calls you found in a csv table with three columns: 
  - filename (i.e. the file where the call occured) and line number in form L[line-number] where the call is made
  - RPC call made (i.e. method name)
  - number of times the rpc call is made. The name of the file should be "[repo_name]_detailed.md"
6. At the end generate an aggregate markdown table in a file named "[repo_name]_aggregate.md" with two columns: 
  - RPC call
  - Aggregate number of calls (i.e. the total number of calls codebase-wide).  
7. For the purposes of generating aggregate stats in point #6 above, lump the stats of eth_getLogs, eth_getFilterLogs, and eth_getFilterChanges together and give it the name "eth_getLogsANY". So if the stats are 1 eth_getLogs call, 1 eth_getFilterLogs call, and 1 eth_getFilterChanges call, you would treat that as 3 eth_getLogsANY calls. This pseudonym "eth_getLogsANY" therefore lumps the stats of all three combined. Note that this is for "[repo_name]_aggregate.md" only. For the detailed stats in #5, tally each of the three seperately. 
8. In both markdown files, sort rows by number of calls, from highest to lowest
9. Save these files in stats/[repo_name]/[filename] .. if the directory doesn't exist create it. 
10. Do NOT make any modifications to the codebase
