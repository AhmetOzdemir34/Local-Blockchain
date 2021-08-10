import random
import sys
import time

from blockchain import Blockchain
import pickle as p
from user import User

def girisYap():
    try:
        users = p.load(open("users.pickle","rb"))
    except EOFError:
        users = []
    if(users != []):
        while True:
            username = input("Username: ")
            password = input("Password: ")
            for i in users:
                if(i.name==username and i.password==password):
                    print("Welcome {}".format(i.name))
                    return i
            print("Not matched")
    else:
        print("No one is registered on Sys. First, register!")
        return None

def register():
    try:
        users = p.load(open("users.pickle","rb"))
    except EOFError:
        users = []

    while True:
        prob = False
        username = input("username: ")
        for i in users:
            if(i.name == username):
                print("Username is used.")
                prob = True
        if(prob):
            continue
        else:
            break

    password = input("password: ")
    newReg = User(username,password)
    users.append(newReg)
    p.dump(users, open("users.pickle","wb"))
    print("All is done :)")

def atzAl(userObj,atz):
    print("***/// Balance: {} ///***".format(userObj.balanceUSD))
    r = random.random()*2+8
    print("***/// 1 ATZ: {} ///***".format(r))
    while True:
        miktar2 = input("ATZ amount to buy: ")
        if float(miktar2)*r <= userObj.balanceUSD:
            userObj.balanceUSD -= float(miktar2) * r
            userObj.balanceATZ += float(miktar2)
            break
        else:
            print("insufficient balance")
    try:
        users = p.load(open("users.pickle", "rb"))
    except EOFError:
        users = []
    for i in users:
        if(i.name == userObj.name):
            i.balanceUSD = userObj.balanceUSD
            i.balanceATZ = userObj.balanceATZ
            atz.AddBlock("{} $BUY {} ATZ | ( {} )".format(i.publicKey, miktar2, time.ctime()))
    p.dump(users, open("users.pickle", "wb"))
    p.dump(atz, open("blockchain.pickle","wb"))
    print("Completed.")

def atzSat(userObj, atz):
    print("***/// ATZ Balance: {} ///***".format(userObj.balanceATZ))
    r = random.random() * 2 + 8
    print("***/// 1 ATZ: {} ///***".format(r))
    while True:
        miktar3 = input("ATZ amount to sell: ")
        if(float(miktar3) <= userObj.balanceATZ):
            userObj.balanceUSD += r * float(miktar3)
            userObj.balanceATZ -= float(miktar3)
            break
        else:
            print("insufficient balance")

    try:
        users = p.load(open("users.pickle", "rb"))
    except EOFError:
        users = []
    for i in users:
        if(i.name == userObj.name):
            i.balanceUSD = userObj.balanceUSD
            i.balanceATZ = userObj.balanceATZ
            atz.AddBlock("{} $SELL {} ATZ | ( {} )".format(i.publicKey, miktar3, time.ctime()))
    p.dump(users, open("users.pickle", "wb"))
    p.dump(atz, open("blockchain.pickle", "wb"))
    print("Completed.")

"""MAIN FONK"""

if __name__ == '__main__':
    userObj = None
    try:
        atz = p.load(open("blockchain.pickle","rb"))
    except EOFError:
        atz = Blockchain()

    while True:
        secim = input("1) Login\n2) Register\n")
        if secim in '12':
            if secim=='1':
                userObj = girisYap()
                if(userObj != None):
                    break
            else:
                register()
        else:
            print("Invalid value!")


    print("Welcome to Blockchain System.")
    menu = "1) ATZ al/sat\n2) Show All Blocks\n3) Check Blockchain\n4) Add USD \n5) Balance\n6) Exit\n"
    while True:
        print(menu)
        sec = input("Choose one: ")
        if sec in "123456":
            if(sec == "1"):
                while True:
                    secim2 = input("1) Buy ATZ\n2) Sell ATZ\n")
                    if secim2 in "12":
                        if secim2 == '1':
                            atzAl(userObj,atz)
                            break
                        else:
                            atzSat(userObj,atz)
                            break
                    else:
                        print("Invalid value.")

            elif(sec == "2"):
                atz.showChain()
            elif(sec=="3"):
                dogrulama = atz.checkChain()
                if(dogrulama):
                    print("Blockchain is working well.")
                else:
                    print("Chain is broken.")
            elif (sec == "4"):
                miktar = input("How much gonna you deposit USD? : ")
                userObj.balanceUSD += int(miktar)
                try:
                    users = p.load(open("users.pickle", "rb"))
                except EOFError:
                    users = []
                for i in users:
                    if i.privateKey == userObj.privateKey:
                        i.balanceUSD = userObj.balanceUSD
                p.dump(users,open("users.pickle","wb"))
                print("Completed.")
            elif (sec == "5"):
                print("***///***///***///")
                print("USD Balance: {}".format(userObj.balanceUSD))
                print("ATZ Balance: {}\n".format(userObj.balanceATZ))
            else:
                sys.exit(1)
        else:
            print("Invalid Value.")