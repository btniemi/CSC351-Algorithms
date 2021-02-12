import ast

# filehandle is the location of the files data on the disk

with open('fileName.txt', 'r') as filehandle:
    mylist = filehandle.readlines()
    mylist = eval(mylist[0])
    #mylist = eval(mylist[1]) #this is the bad case and will get hacked

with open('fileName.txt', 'r') as f:
    mylist1 = f.readlines()
    print(mylist1)
    mylist1 = ast.literal_eval(mylist1[0])

print(mylist[0])
print(type(mylist[0]))

print(mylist1[0])
print(type(mylist1[0]))

# sys.args[1] is the 2nd element in the argument list you can pass in the cmd line arguments list in the command line
