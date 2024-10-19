x=0
for i in range(5,101,5):
    if i%2==0:
        print(i)
    elif i%2!=0:
        x+=i
print(f"a soma dos impares é {x}") 