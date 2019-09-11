object_position = int(input("Input a position between 1 and 10: "))

check_first = 1 	#Makes sure that the first print is correct

def positioning():      #This function is used to "animate" the object

    position_string = ""

    for x in range (1,11):      #prints out x's and an o in the apropriate positon

        if x == object_position:

            position_string +="o"

        else:

            position_string +="x"
        
    return(position_string)

def change_direction(): #This function changes the direction of the object

    direction = input("Input your choice: ")

    if direction == "l":

        if object_position == 1:    #prevents the postionion going under 1
            return 0

        else:
            return -1

    if direction == "r":

        if object_position == 10:   #prevents the position going over 10
            return 0

        else:
            return 1

    if direction != "r" or direction != "l":
        return 100


while object_position >= 1 and object_position <= 10:   #This while loop continues running until object_position goes out of the range 1-10 including 10
    if check_first == 0:

        object_position_buffer = 0

        object_position_buffer += change_direction()

        if object_position_buffer >= -1 and object_position_buffer <= 1:

            object_position += object_position_buffer  

            disp_string = positioning()

            print(disp_string)  
        else:
            disp_string = positioning()

            print(disp_string) 

            object_position += 100
         
    
    else:           # When the while loop is enterd this runs first and only first time through the loop

        disp_string = positioning()

        print(disp_string)

        check_first =0

        print("l - for moving left")
        print("r - for moving right")
        print("Any other letter for quitting")



    




