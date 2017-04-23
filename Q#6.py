#Question No. 6
#Ankit Mittal
#Personal Challenge: Use least lines of code as possible

# Finding the sum of the squares.
a = sum([i**2 for i in range(101)])

# Finding the square of the sum.
b = sum(range(101))**2

print(b - a)
