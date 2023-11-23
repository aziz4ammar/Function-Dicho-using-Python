import numpy as np
def remplir(n):
    for i in range (n):
        x=int(input("T["+str(i)+"]"))
        a=i
        while (a>0)and(x>t[a-1]):
            t[a]=t[a-1]
            a=a-1
        t[a]=x
def dicho (r,d,f,t):
    if (d>f):
        return -1
    else:
        m=(d+f)//2
        if (t[m]==r):
            return m
        elif(t[m]>r):
            return dicho(r,m+1,f,t)
        else:
            return dicho(r,d,m-1,t)
def affiche(n,r,t):
    p=dicho (r,0,n-1,t)
    if p==-1:
        print("sobhan l hay eddeyem")
    else:
        print("la position de"+" "+str(r)+" est "+str(p)+" dans le tableau")
n=12
t=np.array([int]*n)
remplir(n)
print(t)
r=float(input("het float= "))
affiche(n,r,t)

