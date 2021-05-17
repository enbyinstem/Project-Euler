x = 1
y = 1
sum_of_even_fib = 0
while x < 4000000:
    if x % 2 == 0:
        sum_of_even_fib = sum_of_even_fib + x
    a=x
    x=y+x
    y=a
print(sum_of_even_fib)
        
