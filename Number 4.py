def reverse(num):
    return str(num) == str(num)[::-1]
    
i=999
j=999

palindrones = []

while i >= 100:
    while j >= 100:
        product = i *j
        if reverse(product) == True:
            palindrones.append(product)
        j -= 1
    j = 999
    i -= 1
        
print(max(palindrones))
