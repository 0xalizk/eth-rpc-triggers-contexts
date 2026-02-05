### How to replicate this with Claude

1. Clone a repo ([rotki](https://github.com/rotki/rotki), [Kohaku](https://github.com/ethereum/wallet-poc), [helios](https://github.com/a16z/helios)) or scrape a frontend ([aave](https://app.aave.com), [zerion](https://app.zerion.io)):

2. **Write [the skill needed](SKILL.md)** 
  - `mkdir ~/.claude/skills/scrape-rpc-calls`
  - `vim ~/.claude/skills/scrape-rpc-calls/SKILL.md`
  - _Take the time to sharpen it_

3.  [Searched other skills e.g. static analyzer](https://www.skillsdirectory.com/docs) 

4. Go nuts in terminal
  - `claude`
  - prompt: `/scrape-rpc-calls analyze the codebase and find rpc calls in the codebase that is under directory /rotki`
      - _Be sure to reference the skill_ 
  - `! head stats/rotki/*detail*`  #sanity check
  - "Did you skip any rpc calls because you determined they were in a testing context?" >> good answer, correct skipping
  - Prompt it to show its reasoning for including/excluding a certain RPC trigger, eyeball the code to sanity check

5. Repeat for others
  - `! git clone https://github.com/a16z/helios && cd helios` # use '!' to avoid wasting tokens on bash commands

6. [Observed the session](https://claude.ai/settings/usage) to not exceed the "bucket" of usage I have within a given session. If I did, I would stop go get lunch and wait for the bucket to reset (cost reduction thing, if I continue working after session bucket is depleted some more expensive tier of charging kicks in).

7.  <div style="margin-left: 19px;"> <details><summary>&nbsp;  Plot it</summary>
    I want you to create a bar plot from the aggregate stats we have for each codebase under the stats/ directory. So you will read stats from the "*_aggregate.md" files. 
    
    I want to combine multiple rpc calls into a bar as follows: 
    
    I want there to be 4 bars, each bar reflects the lumped statistics of some rpc calls 
    
    State: eth_getBalance, eth_getStorageAt, eth_getCode, eth_call
    
    Receipts: eth_getTransactionReceipt, eth_getLogs, eth_getFilterLogs, eth_getFilterChanges
    
    Transactions: eth_getTransactionCount, eth_getBlockTransactionCountByHash, eth_getBlockTransactionCountByNumber, eth_getTransactionByHash, eth_getTransactionByBlockHashAndIndex, eth_getTransactionByBlockNumberAndIndex
    
    Blocks: eth_getBlockByHash, eth_getBlockByNumber
    
    So for example "State" is one bar whose height reflect the combined number of these rpc calls eth_getBalance, eth_getStorageAt, eth_getCode, eth_call. 

    I want there to be one bar group per codebase. So the groups are: aave, rotki, helios, wallet-poc, and zerion. 
    
    I want you to create a virtual python environment and plot with matplotlib, similar to how plotting was done in this repo: https://github.com/0xalizk/mopro-benchmarks
    
    Borrow what you need from this repo like the matplotlib parameters from update_rcParams() function and beautify_ax() function in https://github.com/0xalizk/mopro-benchmarks/blob/main/src/main.py
    
    Save the generated plot in the current directory as rpc-dist.png.

    Ask me questions if anything is unclear.

</details></div>

**[See more tips here (add yours!)](https://www.notion.so/efdn/Agentic-tips-and-tricks-028d9895554182429bd901a6198ebacc)**
