# Q11.Implement a function named generateRange(min, max, step), which takes three arguments and generates a range of integers from min to max, with the step. The first integer is the minimum value, the second is the maximum of the range and the third is the step. (min < max)
# Task
# Implement a function named

# generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
# generate_range(1, 10, 3) # should return list of [1,4,7,10]
# generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
# generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]
# Note
# min < max
# step > 0
# the range does not HAVE to include max (depending on the step)


def fun(min,max,step):
    i=min
    a=[]
    while i<=max:
        a.append(i)
        i+=step
    print(a)
fun(2,10,2)
fun(1,10,3)
fun(2,10,2)
fun(1,10,3)

            
        