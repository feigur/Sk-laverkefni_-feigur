n = int(input("Enter the length of the sequence: ")) # Do not change this line

number_1 = 1

number_2 = 2

number_3 = 3

counter = 1

check = 1       #Checks what number to print

double_check = 1#Prevents a number from printing twice per loop

while counter <= n:
    if check == 1 and double_check == 1:            
        print(number_1)
        number_1 = number_1 + number_2 + number_3
        check = 2
        double_check = 0
    
    if check == 2 and double_check == 1:
        print(number_2)
        check = 3
        number_2 = number_1 + number_2 + number_3
        double_check = 0

    if check == 3 and double_check == 1:
        print(number_3)
        number_3 = number_1 + number_2 + number_3
        check = 1
        double_check = 0

    double_check = 1
    counter += 1