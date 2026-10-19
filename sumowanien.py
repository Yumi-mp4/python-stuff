n = 20
m = 0
par = []
npar = []
while n>m:
    m+=1
    if m%2==0:
        par.append(m)
    elif m%2!=0:
        npar.append(m)

sumpar=sum(par)
sumnpar=sum(npar)
print(f"{par} {sumpar}")
print(f"{npar} {sumnpar}")

print("======")

print(f"dla liczby n={n} suma parzystych to {sumpar}, a nieparzystych to {sumnpar}")