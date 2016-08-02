n = input("Berapa bintang omz ? ");
a = 0
b = 0
c = n
while(1<=n):
    print " " * (b) + "*" * (n+1) + "*" + "*" * (n-1)
    n = n-1
    b = b+1
print " " * c + "*"
while(1<=c):
    print " " * (c-1) + "*" * (a+1) + "*" + "*" * (a+1)
    c = c-1
    a = a+1