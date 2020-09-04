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

h_double_odds=0
p_double_odds=.1
l_double_odds=.0457

h_triple_odds=1
p_triple_odds=1
l_triple_odds=.0004

h_hr_odds=0
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


#BETTER WAY TO DO PROBABILITY DISTRIBUTIONS????????
def bipsim():
    a=single_odds=(h_single_odds*(p_single_odds/l_single_odds))*100
    b=double_odds=(h_double_odds*(p_double_odds/l_double_odds))*100
    c=triple_odds=(h_triple_odds*(p_triple_odds/l_triple_odds))*100
    d=hr_odds=(h_hr_odds*(p_hr_odds/l_hr_odds))*100
    int1=a
    int2=a+b
    int3=a+b+c
    int4=a+b+c+d
    biptest=random.randint(1,101)
    if biptest <= int1:
        return "single"
    elif int1 < biptest <= int2:
        return "double"
    elif int2 < biptest <= int3:
        return "triple"
    elif int3 < biptest <= int4:
        return "homerun"
    elif int4 < biptest:
        return "field out"


def atbatsim(n):
    result=atbatoutcomes(n)
    if result == "bip":
        return bipsim()
    else:
        return result


#Test block to make sure everything is working.
for i in range(1,100):
    print(atbatsim(100))
    time.sleep(.5)
