n=int(raw_input("input: "))
# n+=1
for i in range(1,n):
    kiri=' '*(n-i)
    kanan='# '*(i)
    gabung=kiri+kanan
    print(gabung)
