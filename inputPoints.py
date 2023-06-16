#SEAH YONG LE STANLEY U2121954F
#input program for user to key in inputs

import turtle as t
import math
pi = math.pi
#define function that detects if lines are self-intersecting

#getting the input
def inputPoints():  
    while True:
        #getting whether user wants to input manually or by clicking the display
        manual = input("If you would like to type the coordinates out, type 'y',if you would like screen clicks, type 'n', else if you would like to input using a file, type 'file':  ")
        p1 = [] #input list

        # if user will like to input manually
        if manual.lower() == "y": 
            boolean1 = True #set condition to break out of while loop later on    
            while boolean1:
                a = input("Please input the coordinates separated by commas (eg x,y), and when done inputting all the coordinates, type 'Done': ") 
                if a.lower() == "done":
                    boolean1 = False # breaks out of the while loop since z becomes false
                else:  
                    try:
                        b = a.split(",") #split code into different chunks separated by commas
                        b[0] = float(b[0])
                        b[1] = float(b[1])#check if input is in terms of numbers
                        p1.append([b[0], b[1]])  # add the point to the polygon list data
                    except IndexError: #if unable to split the input, then will form index error because b[1] wont exist
                        print("Please input a proper coordinate")
                        

            return p1
            break   

        # if user wants to click using the display
        elif manual.lower() == "n":
            s = t.Screen()
            y = t.Turtle()
            y.hideturtle()
            #draw box for coordinates
            boolean2 = True
            while boolean2:
                def space_bar(): #define function space bar that draws line from last click to the first click to end the shape
                    y.goto(p1[0][0], p1[0][1])
                    y.pu()
                    boolean2 = False
                    return boolean2
                def line(x, z):   # function that draws a line to the cursor click
                    y.goto(x,z)
                    y.pd()
                    x = (round(x/10,1))*10#rounds off so values are set to the grid
                    z = (round(z/10,1))*10
                    y.write(str(x) + ", " + str(z)) # write the cursor point coordinate
                    p1.append([x, z]) # add the point to the polygon list data                    
                    s.onkey(space_bar,"space") #if spacebar is clicked, goes back to first coordinate
                    s.listen()
                    return p1
                y.pu()
                s.onclick(line) #calling out function
                break
        #if user wants to input using a data file            
        elif manual.lower() == "file": 
            try:
                a = input ("Please input name of the file: ")
                b = open(a)
                for line in b: #iterate through every line in file
                    line = line.strip("\n") #stripping \n at the back
                    coordinates = line.split(",") #split string from file by ","
                    p1.append([float(coordinates[0]), float(coordinates[1])]) #appending coordinates to list p1
            except FileNotFoundError: #settling errors in input
                print("Please edit the name of file.")

    
        else:
            print("Please key in either a Y or a N or file")


        return p1  #returns the value to the main program           

