

name = input("What is your full name ")
number_school = int(input("Write your school registration number "))
poema = (input("Write a frase or poem more than like this "))


a = "Saul"
b = "me"
c = "La chupa con crema"
d = " ".join([a,b,c])
union = " ".join([poema,d])


name2 = name.upper()
name3 = name.lower()
mus = poema.index("m",0,100)
mus2 = poema.rindex("u",0,100)
encuentra = poema.find("Luis")
list = poema.split()
letter1 = poema[0::]


print(f"your name in mayus this is\n {name2}")
print(f"your name in minus this is\n {name3}")
print(f"the letter m in the poem is in the position\n {mus}")
print(f"the letter u is in the position\n {mus2} ")
print(f"the name luis is in the position\n {encuentra} ")
print(F"The words in poem this\n {list}")
print(f"The first letter in you poem this the letter\n {letter1}")
print(f"{d}")
print(union)




