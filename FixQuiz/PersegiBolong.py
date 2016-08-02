y = input('input : ')
x = ""
c = ""
z = " " * (int(y) - 2)
a = y - 1
b = ""
for j in range(1,y+1):
    x = x + str(j)

print x
for i in range(2,y):
    print str(i) + z + str(a)
    a-=1

for k in range(y,0,-1):
        c += str(k)
print c