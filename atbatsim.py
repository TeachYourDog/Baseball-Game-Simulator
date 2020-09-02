import random
import time



trials=10000

#Probabilities will be calculated using actual data sets, placeholders for now
#Hitter, Pitcher and League probability of strikeouts
hkodds=.210
pkodds=.24
lkodds=.22

hbbodds=.210
pbbodds=.24
lbbodds=.22

hhitodds=.210
phitodds=.24
lhitodds=.22



#Determines whether or not a strikeout occurs
def strikeout():
    ks=0
    kodds=hkodds*(pkodds/lkodds)
    for i in range(1000):
        if random.random() <= kodds:
            ks += 1
        return ks


#simulates at bats n number of times, returning probability of strikeout
def ksim(n):
    trials=[]
    for i in range(n):
        trials.append(strikeout())
    return(sum(trials)/n)



#Determines whether or not a walk occurs
def walk():
    bbs=0
    bbodds=hbbodds*(pbbodds/lbbodds)
    for i in range(1000):
        if random.random() <= bbodds:
            bbs += 1
        return bbs


#simulates at bats n number of times, returning probability of walk
def bbsim(n):
    trials=[]
    for i in range(n):
        trials.append(walk())
    return(sum(trials)/n)


#Determines whether or not a hits occurs
def hit():
    hits=0
    hitodds=hhitodds*(phitodds/lhitodds)
    for i in range(1000):
        if random.random() <= hitodds:
            hits += 1
        return hits


def atbatsim(n):
    x=ksim(n)*100
    y=bbsim(n)*100
    test=random.randint(1,101)
    if test <= y:
        return "walk"
    elif test > x+y:
        return "bip"
    else:
        return "strikeout"

for i in range(1,100):
    print(atbatsim(1000))
