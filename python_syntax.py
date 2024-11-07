#-----INPUT AND OUTPUT IN PYTHON-----

#input of multiple numbers, map them to a type
# x, y, z = map(int, input("enter x, y, z: \n").split())

#when printing multiple values, need to group them up like (x, y, z), can mix different types of values 
#print("output is: %f %d %f" %(x, y, z))
#or you can just use fstring
# print(f"output is: {x: f} {y: d} {z: f}")

#-----FUNCTIONS IN PYTHON-----

# def square(x):
#     return x ** 2

#this is also a way to define the type of a function
#def square(x) -> int:
#   return x**2 

# def printList(*ls):
#   for x in ls:
#       print(x)
#
#   def printOdd():
#       for x in ls:
#           if (x % 2)
#               print(x)