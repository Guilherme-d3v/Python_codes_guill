import random
r1 = random.randint (20,50)
r2 = random.randint (20,50)
r3 = random.randint (20,50)
r4 = random.randint (20,50)

if r1<r2 and r1<r3  and r1<r4:
    p1= r1
    if r2<r3 and r2<r4:
        p2=r2
        if r3>r4:
            p3, p4 = r3,r4
        else:
            p3, p4 = r4,r3
    elif r3<r2 and r3<r1:
        p2=r3
    elif r1<r2 and r1<r3:
        p2=r1
elif r2<r1 and r2<r3 and r2<r4:
    p1= r2
elif r3< r1 and r3<r2  and r3<r4:
    p1= r3
else:
    p1=r4