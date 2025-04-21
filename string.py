a="challagali chandrika" #Strings are Arrays
print(a[2])

for y in "apple":   #for loop
    print(y)

a="anusha"    #len()
print(len(a))

a= "my life is full of problems " #Check in String
print("problems" in a) 

b="python"
print("y" in b) 

a="python is awesome"  # check not in
print("java" not in a)

a="challagali ajay"   #Slicing Strings
print(a[2:3])
print(a[:4])
print(a[2:])
print(a[-2:-5])

a="challagali chandrika"  #Modify Strings
print(a.upper())

b="ANUSHA"
print(b.lower())

c="hello world"   # strip()removes any whitespace 
print(c.strip)

d= "challagali chandrika"
print(d.replace("c" , "s"))

e="challagali anusha"
print(e.split(", "))

a= "apple" #String Concatenation
b= "banana"
c= a+b
print(c)

p="narendra"
q="pavani"
r= a + "   "+b
print(r) 

age=25  #String Format
w="my name is chandrika, I am" + age
print(w) #wrong combination using f-strings 

age = 25
w = f"my name is chandrika , I am " + {age}
print(w)

price = 100
a= f"The price is {price}dollars"
print(a)

price = 200
b= f"the price is {price:.2f} dollars"
print(b)

c= f"the price is{20*30}dollars"
print(c)

#Escape Character

a="chandrika is \"z\" " #double quotes 
print(a)

b='it\'s a joke'  #Single Quote
print(b)

c="chandrika \\challagali " #Backslash
print(c)

d="ajay\nyadav"  #New Line
print(d)

e="anus..........ha\ryadav"  #	Carriage Return
print(e)

f="ramu\tyadav"   #Tab
print(f)

g="hello \bworld" #Backspace
print(g)
 
txt = "\110\145\154\154\157"  #\ooo Octal value
print(txt)

txt = "\x48\x65\x6c\x6c\x6f" #\xhh	Hex value
print(txt) 