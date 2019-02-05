Sum_of_squares = 0
x = 0
Square_of_sum = 0

for i in range(1, 101):
    Sum_of_squares += i
    x = i * i
    Square_of_sum += x

print((Sum_of_squares * Sum_of_squares) - Square_of_sum)