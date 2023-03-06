import random


def mark6():
    allnum = list(range(1,50))

    output = []
    while True:
        num=random.choice(allnum)
        output.append(num)
        allnum.remove(num)
        if len(output) >= 6:
            return sorted(output)
    

def generator():
    ManyOutput=[]
    while True:
        output = mark6()
        ManyOutput.append(output)
        if not (output in ManyOutput):
            ManyOutput.append(output)
        if len(ManyOutput) >= k:
            return ManyOutput
    

def getk():
    k=input('要生成多少次?\nHow many time you want to generate?\n')
    if not k.isdigit():
        k=1
    return int(k)


k=getk()
for output in generator():
    print(output)
