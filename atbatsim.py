import random
import time


trials=10000

#League odds are fixed per year, player and pitcher odds calculated from datasets

#Hitter, Pitcher and League probability of strikeouts
h_k_odds=.210
p_k_odds=.24
l_k_odds=.2295

h_bb_odds=.210
p_bb_odds=.24
l_bb_odds=.0852

h_single_odds=.10
p_single_odds=.1
l_single_odds=.1391

h_double_odds=.1
p_double_odds=.1
l_double_odds=.0457

h_triple_odds=.1
p_triple_odds=.1
l_triple_odds=.0004

h_hr_odds=.1
p_hr_odds=.1
l_hr_odds=.0363


outs=0

#Determines whether or not a strikeout occurs
def strikeout():
    ks=0
    k_odds=h_k_odds*(p_k_odds/l_k_odds)
    for i in range(1000):
        if random.random() <= k_odds:
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
    bb_odds=h_bb_odds*(p_bb_odds/l_bb_odds)
    for i in range(1000):
        if random.random() <= bb_odds:
            bbs += 1
        return bbs


#simulates at bats n number of times, returning probability of walk
def bbsim(n):
    trials=[]
    for i in range(n):
        trials.append(walk())
    return(sum(trials)/n)



def atbatoutcomes(n):
    x=ksim(n)*100
    y=bbsim(n)*100
    test=random.randint(1,101)
    if test <= y:
        return "walk"
    elif test > x+y:
        return "bip"
    else:
        return "strikeout"

def bipsim():
    a=single_odds=(h_single_odds*(p_single_odds/l_single_odds))*100
    b=double_odds=(h_double_odds*(p_double_odds/l_double_odds))*100
    c=triple_odds=(h_triple_odds*(p_triple_odds/l_triple_odds))*100
    d=hr_odds=(h_hr_odds*(p_hr_odds/l_hr_odds))*100
    biptest=random.randint(1,101)
    if biptest <= a:
        return "single"
    elif a < biptest <= b:
        return "double"
    elif b < biptest <= c:
        return "triple"
    elif c < biptest <= d:
        return "homerun"
    else:
        return "out"


def atbatsim(n):
    if atbatoutcomes(n) == "bip":
        return bipsim()
    else:
        return atbatoutcomes(n)


#Test block to make sure everything is working. It does!!!!!!
for i in range(1,100):
    print(atbatsim(100))
    time.sleep(.5)
