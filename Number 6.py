def diff(n):
    sum_of_square = (n*(n-1)/2) ** 2
    square_of_sum = 0
    for i in range(n+1):
        square_of_sum += i ** 2
    return sum_of_square - square_of_sum

if __name__ == "__main__":
    print(diff(100))
