k = 1
o = 8
kosong = " "
print kosong * (o + 1) + "*"
while(k<=o):
    print " " * (o + 1 - k), "*" * k * 2
    k +=1