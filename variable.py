#creating or declaring variable:

a="chandrika"
b= 24
c= 3.14
d=True
print(a,b,c,d)
print(a,b,c,d,sep="  ")

# Type()of variable:

a = "chandrika"
b = 'a'
c ='aaaa' 
d = 55
e = 3.14
f = True
print(type(a),type(b),type(c),type(d),type(e),type(f))

#casting variable :

a=int(55)
b=int(3.14)
c=int(True)
d=int(False)
e=int(a)
f=int("25")
print(a,b,c,d,e,f)

p=float(25)
q=float("30")
r=float(True)
s=float(False)
print(p,q,r,s)

m=str(30)
n=str(3.14)
k=str(4+3j)
o=str(True)
p=str(False)
q=str("chandrika")
print(m,n,o,p,q)


#case-sensitive:

AGE=25
Age=20
age=30
print(AGE,Age,age)


#multiple valuse:

a,b,c,d= 25,"ajay","apple",-20
print(a)
print(b)
print(c)
print(d)

p=q=r=s="chandrika"
print(p)
print(q)
print(r)
print(s)

valuse=(1,2,3,4) #Unpack valuse
x,y,z,w=valuse
print(x)
print(y)
print(z)
print(w)

