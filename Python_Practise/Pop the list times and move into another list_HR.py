a=['1234567891','12345678985','45678','14578123','teja','bujji','afsfaaaade','qwertyasdf','123456qwer']
b=[]
for j in range (len(a)):
    for i in a:
        if len(i)==10:
            pass
        else:
            c= a.index(i)
            #print(c)
            b.append(i)
            a.pop(c)
        #c=c+1
        #print(a)
print(a)
print(b)
