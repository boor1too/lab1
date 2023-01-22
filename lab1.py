#syntax
print("Hello World")

if 5 > 2:
    print("Five is greater than two!")

#comments
    #this is a comment

    '''
    this is a comment
    written in
    more than just one line
    '''

#variables
    carname = "Volvo"

    t = 50

    x = 5
    y = 10
    print(x + y)

    z = x + y
    print(z)

    myfirst_name = "John"

    a = b = c = "Orange"

    def myfunc():
        global g
        g = "fantastic"

#data types
    m = 5  #int

    n = "Hello world"  #str

    v = 20.5  #float

    h = ["apple", "banana", "cherry"]  #list

    k = ("apple", "banana", "cherry")  #tuple

    l = {"name" : "John", "age" : 36}  #dict

    j = True  #bool

#numbers
    p = 5
    p = float(x)

    i = 5.5
    i = int(i)

    u = 5
    u = complex(u)

#strings
    d = "Hello world"
    print(len(d))   #length

    txt = "Hello world"
    print(txt[0])   #first character

    print(txt[2:5])

    txt.strip()  #remove whitespaces

    txt.upper()  #uppercase

    txt.lower()  #lowercase

    txt = txt.replace("H","J")

#booleans
    print(10 == 9)  #false

    print(bool("abc"))  #true

    print(bool(0))  #false

#operators
    print(10 / 2)

    print(10 * 2)

    fruits = ["apple", "banana"]
    if "banana" in fruits:
        print("Yes, banana is a fruit")

    if 5 != 10:
        print("5 is not equal to 10")

    if 5 == 10 or 4 == 4:
        print("At least one of statements is true")

#if...else
    r = 10
    e = 5
    if r == e:
        print("r equals e")
    elif r <= e:
        print("e is not less than r")
    else:
        print("r is bigger than e")