s=input("Enter string: ")
p=s.split("")
for i in range(0,len(p)):
  r=p[i]
  if "A" in r or "a" in r:
    print(r)
