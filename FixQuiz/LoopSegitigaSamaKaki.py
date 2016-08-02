n=int(raw_input("input: "))
a=0
#print " "*(n)+"#"
for i in range(n,0,-1):
 print (' '*(i)+'#'*(a+1)+'#'*(a+1))
 a=a+1