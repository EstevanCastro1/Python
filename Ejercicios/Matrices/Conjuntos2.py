a=[["A","B"]],[["A","X"]],[["B","Z"]]
b=[["A","X"]],[["D","S"]],[["Y","Z"]]
c=[]

for j in a:
    for r1 in j:
        for r2 in b:
            for r3 in r2:
                if r1==r3:
                    if c.count(r1):
                        break
                    else:
                        c.append(r1)
print(c)
