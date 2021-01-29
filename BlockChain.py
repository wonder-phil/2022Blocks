from Block import *
import copy

class BlockChain:
    blockChain = []
    genesisBlock = Block("empty","genesis block")
    dataList = ["a","b","c","d","e","f","g"]

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

    def validateBlockChain(self):
        valid = True
        b = self.blockChain[0]
        if b != genesisBlock:
            valid = False
        temp = copy.deepcopy(b)
        lastHash = temp.compHash()
        if valid:
            for b in self.blockChain[1:]:
                if b.prevHash != lastHash:
                    valid = False
                else:
                    temp = copy.deepcopy(b)
                    lastHash = temp.compHash()
                
        return valid
            
    
