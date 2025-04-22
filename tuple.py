a = (1,2,1,'3',"chandrika",-1)
print(a)

a.index(a[0]) # Accessing Tuple with Indexing 
a.index(a[-1])
print(len(a))
print(a[0:2]) #slicing
print(a[:2])
print(a[2:])

b = ("22","anusha",3,4) # Tuple unpacking
c,d,e,f = b
print(c)
print(d)
print(e)
print(f)

a=(1,2,3,"chandrika") #Concatenation Tuples
b=(22,33,44,"anusha")
c=(a + b)
print(c)

p= (0,9,8,7) # nested tuples
q= ("ajay","anu")
r= (p,q)
print(r)

a=("chandrika",) # Creating a Tuple with repetition
print(a*5)

