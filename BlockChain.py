from Block import *

class SmallBlockChain:
    smallChain = []
    genesisBlock = Block(1,"First Block","")
    dataList = ["a","b","c"]

    def compSmallBlockChain(self, totalBlocks, difficulty):
        self.smallChain.append(self.genesisBlock)
        for i in range(totalBlocks):
            newBlock = self.smallChain[i].mineBlock(difficulty);
            newBlock.update(self.smallChain[i].bHash,self.dataList[i])
            newBlock.compHash()
            self.smallChain.append(newBlock)

    def printChain(self):
        for b in self.smallChain:
            print(b.bHash)
            
    
