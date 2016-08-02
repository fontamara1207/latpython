userInput = int(input("input: "))
row = 0
while(row < userInput):
    row += 1
    spaces = userInput - row
    spaces_counter = 0
    while(spaces_counter < spaces):
        print" ", ''
        spaces_counter += 1
        num_stars = 2*row-1
        while(num_stars > 0):
         print"*", ''
         num_stars -= 1
    print"\n"