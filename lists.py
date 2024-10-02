# CLASS 5
# in python list you can store any data type
var1 = [4, 5, 6, 7, 8.5, 'c', "hi"]
print(var1)
print(type(var1))
# indexing
print(var1[5])
print(type(var1[5]))
# negative indexing
print(var1[-1])
print(var1[-2])
print(var1[-3])
print(var1[-4])
print(var1[-5])
print(var1[-6])
var2 = ["Ganga", "Joshi", 34, var1]
print(var2)
# access list/element inside list
print(var2[3])
# access character in str
print(var2[0][3])
var3 = []
var3.append(3)
var3.append(4)
# append list on list
var3.append(var2)
var3[2].append("Fynd")
var3[2][3].append("Fynd")
print(var3)
# Delete element/list inside list
del var3[1]
print(var3)

# Initializing all index places at a time
arr1 = []
for i in range(10):
    arr1.append(0)
print(arr1)
arr1_1 = ["Fynd"]*10
print(arr1_1)

# Slicing of list
arr1 = [0,1,2,3,4,5,6,7,8,9]
# end excluded in slicing range
print(arr1[1:6])
print(arr1[3:])
print(arr1[:5])
# step/jump
print(arr1[0:10:2])
print(arr1[0:10:3])
# reverse
print(arr1[-1:-7:-1])
# non reverse
print(arr1[-7:-1:1])
print(arr1[-7:-1:-1])
a = slice(2, 8, 2)
print(arr1[a])
print(arr1[slice(2,8,2)])

y = "The quick brown fox jumps over the lazy dog"
print(y[:9])
print(y[10:])
print(y[-10:])

def myfunc(x):
    arr = [0,1,2,3,4,5,6,7,8,9]
    return arr[x]
def myfunc2(x1, x2):
    arr = [0,1,2,3,4,5,6,7,8,9]
    return arr[x1:x2]

mySlice = slice(1,3)
# myfunc(slice(1,3))
print(myfunc(mySlice))
myfunc2(2,6)

print(len(arr1))

arr=[]
for i in range(10):
    arr.append("hello "+str(i))
print(arr)

for i in arr:
    print(i)

for i in range(len(arr)):
    print(i)
    if i==3:
        arr[i] = "Ganga Joshi"
    print(arr[i])

# Write the code to find if a particular element exist in a list
# inout= arr, x

# def checkValue(arr, x):
#     for i in arr:
#         if(i==x):
#             return True
#     return False
def checkValue(arr, x):
    for i in range(len(arr)):
        if(arr[i]==x):
            return True
    return False
        
arr = [0, 2,"Hi", 5, 7]
ans = checkValue(arr, "Hi")
print(ans)

# print(help(list))
# builtin function in python

# Join two list
a=[1,2,3]
b=[4,5,6]
c = a+b
print(c)

for i in b:
    a.append(i)
print(a)
print(b)

arr = [60, 5, 78, 3, 1, 2, -10, 50]
arr.sort(reverse=True)
print(arr)
arr = [60, 5, 78, 3, 1, 2, -10, 50]
arr2 = sorted(arr)
print(arr)
print(arr2)
arr = [60, 5, 78, 3, 1, 2, -10, 50]
arr2 = sorted(arr, reverse=True)
print(arr)
print(id(arr))
print(arr2)

