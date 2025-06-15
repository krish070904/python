#these are immutable means we cant change it directly
a =(1,2,343,3424,False)
print(a)
print(type(a))
print(a.count(2))#counts the no. of occurence of the given value in tuple

i = a.index(343)#gives the index of the first occurence of the given value
print(i)

my_tuple = (1,2,3)
repeated = my_tuple * 3
print(repeated)

print(2 in my_tuple)#check if an item exists in a tupple , returns in true or false

print(len(a))#lgnth of the tuple

sliced = my_tuple[1:2]
print(sliced)

a, b, c = my_tuple
print(a, b, c)