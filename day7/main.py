import time

# Finding fibonacci number using recursion
def fibonacci_recursion(n):
    if(n==0 or n==1):
        return n
    return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)

# Finding fibonacci number using Dynamic Programming
fibonacci_dict={0:0,1:1}
def fibonacci_using_dp(n):
    if(n==0 or n==1):
        return n
    elif n in fibonacci_dict:
        return fibonacci_dict[n]
    else:
        fibonacci_dict[n]=fibonacci_using_dp(n-1)+fibonacci_using_dp(n-2)
        return fibonacci_dict[n]

# Finding fibonacci number using Decorator
def fibonacci_using_decorator(fibonacci):
    cache={}
    def store_in_cache(x):
        if x in cache:
            return cache[x]
        else:
            cache[x]=fibonacci(x)
            return cache[x]
    return store_in_cache

@fibonacci_using_decorator
def fibonacci(n):
    if(n==0 or n==1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

with open("output.txt", "a") as f:

    start_time=time.time()
    print("Output = ",fibonacci_recursion(10),file=f)
    end_time=time.time()
    print("Time take by recursion - ",end_time-start_time,file=f)

    start_time_using_dp=time.time()
    print("Output = ",fibonacci_recursion(10),file=f)
    end_time_using_dp=time.time()
    print("Time take by DP - ",end_time_using_dp-start_time_using_dp,file=f)

    start_time_using_decorator=time.time()
    print("Output = ",fibonacci(10),file=f)
    end_time_using_decorator=time.time()
    print("Time take by Decorator - ",end_time_using_decorator-start_time_using_decorator,file=f)

