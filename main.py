from connected_shapes import Shape, ConnectedShape    


foo = ConnectedShape()
print("/////////////////////////////////////////")
foo.add_shape(Shape('circle', 'Red', 10))
foo.add_shape(Shape('sqaure', 'Blue', 1))
foo.add_shape(Shape('sqaure', 'Black', 25))
foo.add_shape(Shape('circle', 'Green', 6))
foo.add_shape(Shape('sqaure', 'Yellow', 3))
foo.add_shape(Shape('sqaure', 'Red', 15))
print(foo)
print("/////////////////////////////////////////")

while(True):
    print("################################")
    print(f"Connected Shapes. Enter your choice to continue")
    print(" 1. Display all shapes")
    print(" 2. Area of a specific shape")
    print(" 3. Area sum")
    print(" 4. Modify color")
    print(" 5. Modify dimension")
    print(" 6. Dump connected config to a json file")
    print("################################")
    user_choice = input()
    if user_choice not in ['1','2','3','4','5','6']:
        print("Please enter a valid option")
        continue

    else:
        user_choice = int(user_choice)

    if user_choice == 1:
        foo.display_shape()
        
    elif user_choice == 2:
        identifier = input("Shape you want to compute the area: ")
        foo.display_area_shape(identifier) 
        
    elif user_choice == 3:
        foo.sum_area()
        
    elif user_choice == 4:
        foo.display_shape()
        identifier = input("For which shape you want to modify the color: ")
        color = input("Color you want to modify: ")
        foo.update_color(identifier, color)
        foo.display_shape()
        
    elif user_choice == 5:
        foo.display_shape()
        identifier = input("For which shape you want to modify the dimension: ")
        dimension = input("Dimension you want to modify: ")
        foo.update_dimension(identifier, dimension)
        foo.display_shape()
    
    elif user_choice == 6:
        foo.dump_to_json()
    
    else:
        print("Not a valid option")

    print("-----------------------------------")
    print("-----------------------------------")
    print("Press q to quit and c to continue")
    print("-----------------------------------")
    user_choice2 = ""
    while(user_choice2!="c" and user_choice2!="q"):
        user_choice2 = input()
        if user_choice2 == "q":
            exit()

        elif user_choice2 == "c":
            continue