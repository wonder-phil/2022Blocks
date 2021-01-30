from Block import *

b=Block("empty","genesis block")

newBlock=b.mineBlock(5)
print("start:"+newBlock.bHash+":end")
