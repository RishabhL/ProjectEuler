Current_number = 1
Previous_number = 0
Next_number = 0
x = 0

while Current_number < 4000000:
    Previous_number = Current_number
    Current_number = Next_number
    Next_number = Previous_number + Current_number
    print(Current_number)
    if Current_number % 2 == 0:
        x += Current_number


print(x)