from Block import *

class BlockChain:
    blockChain = []
    genesisBlock = Block("empty","genesis block")
    dataList = ["a","b","c"]

    def compBlockChain(self, totalBlocks, difficulty):
        newBlock = self.genesisBlock
        self.blockChain.append(self.genesisBlock)
        for i in range(0,totalBlocks -1):
            newBlock = Block(newBlock.bHash,self.dataList[i])
            newBlock = newBlock.mineBlock(difficulty);
            self.blockChain.append(newBlock)

    def printBlockChainHashes(self):
        for b in self.blockChain:
            print(b.bHash)

    def validateChain(self):
        valid = True
        b = self.blockChain[0]
        if b.data != "genesis block":
            valid = False
            print(1)
        if b.prevHash != "empty":
            valid = False
            print(2)
        if b.bHash != b.compHash():
            valid = False
            print(3)
        lastHash = b.compHash()
        if valid:
            for b in self.blockChain[1:]:
                if b.prevHash != lastHash:
                    valid = False
                    print(b.bHash)
                else:
                    lastHash = b.compHash()
                    print(b.bHash)
                
        return valid
            
    