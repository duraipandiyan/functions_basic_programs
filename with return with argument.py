def myfun1(a,b,c,d):
    name=a
    Age=b
    Address=c
    contact=d
    print("name:",name)
    print("age:",Age)
    print("Address:",Address)
    print("contact",contact)
    store=a,b,c,d

    return store

name = str(input("enter the a Name:"))
Age= int(input("enter the a Age:"))
Address= str(input("enter the a Address:"))
contact= int(input("enter the a contact:"))
v=myfun1(name,Age,Address,contact)
print("biodata:",v)