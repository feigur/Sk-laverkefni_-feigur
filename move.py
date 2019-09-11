object_position = int(input("Input a position between 1 and 10: "))

object_position -= 1

check_first = 1

def positioning():
    position_string = ""
    for x in range (0,10):
        if x == object_position:
            position_string +="o"
        else:
            position_string +="x"
        
    return(position_string)

def change_direction():
    direction = input("Input your choice: ")
    if direction == "l":
        if object_position == 0:
            return 0
        else:
            return -1
    if direction == "r":
        if object_position == 9:
            return 0
        else:
            return 1
    if direction != "r" or direction != "l":
        return 100


while object_position >= 0 and object_position <= 9:
    if check_first == 0:
        object_position += change_direction()
        if object_position > 9:
            break
        disp_string = positioning()
        print(disp_string)   
    
    else:
        disp_string = positioning()
        print(disp_string)
        check_first =0
        print("l - for moving left")
        print("r - for moving right")
        print("Any other letter for quitting")



    




