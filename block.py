import hashlib

class Block():

    def __init__(self, data, timestamp, previousHash=("Not Available.")):
        self.previousHash = previousHash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.createHash()

    def createHash(self):
        hsh = hashlib.sha256((str(self.data) + str(self.timestamp)).encode()).hexdigest()
        return hsh
