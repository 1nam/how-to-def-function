# basics of def a function
def hi():
    print("hello")
hi()

#def a function..........................
def f():
    print("Welcome")
f()

# or more advanced...................
def f(user):
    print(user + " Welcome")
f("ken")

# more............................
def f(user):
    print(user + " Welcome")
f("zeus")
f("1nam")

# even more advanced...............
def soda(name, price):
    print("soda " + name + ",cost " + price)
soda("pop", "$3.00")

# also could do it this way as a string
def soda(name, price):
    print("soda " + name + ",cost " + str(price))#added string
soda("pop", 3.00)# changed quotes
