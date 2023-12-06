#using python lambda function create a fibonacci series from 1 to 50

def fibonacci(count):
 fib_list = [0, 1]     #intializing f0=0 and f1=1 in a list

#adding next element to previous element and appending it to fib_list

 any(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2, count))) 

 return fib_list[:count]

print(fibonacci(50))