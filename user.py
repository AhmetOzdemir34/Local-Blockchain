import hashlib

class User():

    def __init__(self, name,password):
        self.name = name
        self.password = password
        self.balanceATZ = 0
        self.balanceUSD = 0
        self.publicKey = hashlib.sha256(str(self.name+self.password).encode()).hexdigest()[0:10]
        self.privateKey = hashlib.sha256(str(self.name+self.password).encode()).hexdigest()[-1:-11]
