x = 1
sum_of_x = 0
while x < 1000:
    if x % 3 == 0 or x % 5 == 0:
        sum_of_x=sum_of_x+x
    x=x+1
print(sum_of_x)
