x = int(input('podaj pierwsza liczbe  '))
y = int(input('podaj druga liczbe  '))
z = int(input('podaj trzecia liczbe  '))
n = int(input('podaj czwarta liczbe '))
print([[a,b,c,] for a in range(0,x+1) for b in range (0,y+1) for c in range (0, z+1) if a + b + c != n])