#arithmetic opretors
x=11
y=3

print(x+y)
print(x-y)
print(x*y)
print(x%y)
print(x/y)
print(x//y)
print(x**y)

#assigmnt opretors

a=10
a=10
a+=10
a*=2
a-=10
a/=10
a**=10
a//=10

#comparisonn opretors
a=20
b=20
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a>b)
print(a<b)

#logical opretors
a=False
b=False
print(a and b)
print( a or b)
print(not(a))

#membership opretors
c=["a","b","c"]
print("n"in c)
print("n" not in c)

#identity opretors

a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)

#string slicing
s="Hello,MY,World!"
print(s[0:5])
print(s[-6:-1])
print(s[0:12:2])
print(s[::-1])

#modifying string
s="hello,kerala"
new_s=s.replace("kerala","malappuram")
print(new_s)

#string concatnation
s1="hello"
s2="bro"
result=s1+","+s2+"!"
print(result)

words=["python","is","awesome"]
sentences=" ".join(words)
print(sentences)

#string method
s= "Hello,World"
print(len(s))

s=" Hello,World "
print(s.strip())

s="Hello,World"
print(s.split())

s="Hello,World"
print(s.find("H"))

s="Hello,World"
print(s.count("Hello"))

s="Hello,World"
print(s.startswith("Hello"))
print(s.endswith("World"))

s="Hello,World"
print(s.upper())
print(s.lower())

s="Hello,World"
print(s.replace("World","Python"))


s="hello123"
print(s.isalnum())

s="python"
print(s.capitalize())

s="hello world"
print(s.title())

s="python"
print(s.replace("o",""))



