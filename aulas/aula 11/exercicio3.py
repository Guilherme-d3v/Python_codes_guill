def conversor (c):
    return c * 1.8 + 32

temp=int(input('diga a temperatura '))
calc=conversor(temp)
print('a temperatura convertida é ',calc,'°F')