import random
r1 = random.randint (20,50)
r2 = random.randint (20,50)
r3 = random.randint (20,50)
r4 = random.randint (20,50)

if r1>r2:
    r1,r2 = r2,r1
if r1>r3:
    r1,r3 = r3,r1
if r1>r4:
    r1,r4 = r4,r1
if r2>r3:
    r2, r3 = r3 , r2
if r3>r4:
    r3, r4 = r4, r3
print ({r1},{r2},{r3},{r4})