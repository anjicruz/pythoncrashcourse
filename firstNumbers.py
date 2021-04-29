for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

evenNumbers=list(range(2,11,2))
print(evenNumbers)

squares=[]
for value in range(1,11):
    #square=value**2
    squares.append(value**2)
print(squares)

squares=[value**2 for value in range(1,11)]
print(squares)

                        