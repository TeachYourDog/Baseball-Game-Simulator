from random import randint

trials=100000


kprob=1
walkprob=2
hitprob=3

strikeouts=0
walks=0
hits=0


for trial in range(trials):
    pitch=randint(1,3)
    if pitch == kprob:
        strikeouts += 1
    elif pitch == walkprob:
        walks += 1
    elif pitch == hitprob:
        hits +=1

print(strikeouts)
print(walks)
print(hits)
