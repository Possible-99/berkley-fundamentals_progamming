#Range is not a list
nums = range(10)
print(type(nums))
nums = list(nums)
print(type(nums))

# Get the min/max of the whole list
print(min(nums))
print(max(nums))

#Add the elements of one list to another
nums2 = [1,2,3,4]
print(nums + nums2)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]

#String  -> list os substr
sentence = "Hello World 2"
sentence = sentence.split(" ")
print(sentence)
#['Hello', 'World', '2']

sentene = "".join(sentence)
print(sentence)
#['Hello', 'World', '2']



#Selecting and slicing


L = [2,0,9,10,11]
S = "Hello, World"

print(L[2] == 9)
#True

# Get the last element
print(L[len(L) - 1] == 11)
#True
print(L[-1] == 11)
#True


#Slicing
# [a,b) , I think the did it like this to support vector operations where we start from 0
print(L[1: 4]) # 4 - 1 = 3 , for close-open, b - a
#[0, 9, 10]

print(S[1:2] == S[1] == "e")
#True

#With three params , the last one I think work as what char you want to include from this range, only the odd :2
# Like how many steps after the first element
print(S[0:5:3])
# "Hl"