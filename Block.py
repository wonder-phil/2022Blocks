import datetime
import hashlib

class Block:
    hashFunction = ""
    bHash = ""
    def __init__(self,prevHash, data):
        self.prevHash = prevHash
        self.data = data
        self.time = datetime.datetime.now()
        self.nonce = 0
        self.bHash = self.compHash()

    def compHash(self):
        hashFunction = hashlib.new('sha256')
        myStr = str(self.prevHash)+str(self.data)+str(self.time)+str(self.nonce)
        myBytes = myStr.encode()
        hashFunction.update(myBytes)
        self.bHash = hashFunction.hexdigest()
        return self.bHash

    def mineBlock(self,diff):
        self.target = "0"*diff
        while self.bHash[0:diff] != self.target:
            self.nonce = self.nonce + 1
            self.compHash()
        #print("Block mined: ", self.bHash)
        return self

    def update(self,prevHash,data):
        self.prevHash = prevHash
        self.data = data

    def __str__(self):
        s = 'prevHash: '+ self.prevHash + '\n'
        s = s + 'data: ' + self.data + '\n'
        s = s + 'time: ' + str(self.time) + '\n'
        s = s + 'nonce: ' + str(self.nonce) + '\n'
        s = s + 'bHash: ' + self.bHash + '\n'
        return s
