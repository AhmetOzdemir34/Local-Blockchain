import pickle as p
from blockchain import Blockchain
try:
    bc = p.load(open("users.pickle","rb"))
except EOFError:
    bc = []

for i in bc:
    print(i.balanceUSD)