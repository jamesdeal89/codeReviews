# datatypes
myTuple = (1,2,3,4) # mutiple items in a list-like structure however immutable 
mySet = {1,2,3,4} # unordered, multiple items, items must be unique, mutable
myDict = {0:"A",1:"B",2:"C"} # key-value pairs of data, data acessed using the key which is unique

a=3
# switch / case is a more compact version of if/else statements for multiple branches
# requires python 3.10.XX
match a:
    case 1:
        print("a is 1")
    case 2:
        print("a is 2")
    case 3:
        print("a is 3")
    case 4:
        print("a is 4")

# iteration
# for loops are count controlled i.e. we step through a number of items sequentially
for i in range(10):
    print(i)
# while loops are boolean controlled i.e if a condition is true it will continue
while True:
    print("AAA")
x=1
while x == 1:
    print("BBB")
    x=2

# enumerate for lists 
# returned as a tuple
myList = ["Henry","Alex","Xavier"]
for index, name in enumerate(myList):
    print(f"name:{name}, index:{index}")