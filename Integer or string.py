#Python code using lambda function to check every elemt in a list is Integer or string

from functools import reduce

test_list = [[5,6,3],["Gfg", 3, "is"],[9, 'best', 4]]

print("The original list : " + str(test_list))   #printing originl list

#checking if the element in test_list is string
res = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, str)], test_list, [])

print("The string instances : " + str(res))

#checking if the element in test_list is integer 
res1 = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, int)], test_list, [])

print("The string instances : " + str(res1))