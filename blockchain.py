import time
from block import Block

class Blockchain():

    def __init__(self):
        self.chain = [self.createGenesis()]

    def createGenesis(self):
        return Block("GENESIS-BLOCK",time.ctime())


    def AddBlock(self, data):
        node = Block(data, time.ctime(),self.chain[-1].hash)
        self.chain.append(node)

    def checkChain(self):
        for i in range(len(self.chain)):
            if(i>0):
                this = self.chain[i].previousHash
                that = self.chain[i-1].hash
                if(this != that):
                    return False
        return True

    def showChain(self):
        for i in range(len(self.chain)):
            print("****************BLOCK {}*************************".format(i))
            print("Hash: {}".format(self.chain[i].hash))
            print("Previous Hash: {}".format(self.chain[i].previousHash))
            print("DataExpression: {}".format(self.chain[i].data))
        print("***////***////\n\n")