n = input("Berapa bintang omz ? ");
a = 0
b = 0
c = n
for i in range (0,n,1):
    print " " * (b) + "*" * (n+1) + "*" + "*" * (n-1)
    n = n-1
    b = b+1
print " " * c + "*"
for j in range (0,c,1):
    print " " * (c-1) + "*" * (a+1) + "*" + "*" * (a+1)
    c = c-1
    a = a+1