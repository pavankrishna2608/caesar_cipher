#caesarcipher

c="PHHW PH DIWHU WKH WRJD SDUWB"

alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#out=""

k=0

for a in range(1,27):
    out=""
    for i in c:
        if i!=" ":
            k=alf.index(i)
    #print(k) 
            if k+a<=(len(alf)-1):
                out=out+alf[k+a]
            else:
                k=k-26
                out=out+alf[k+a]
    print(a,"\n",out)
    
    

