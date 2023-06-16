#SEAH YONG LE STANLEY U2121954F
import math
import turtle as t
from inputPoints import inputPoints
pi = math.pi

#setting up of turtles
z = t.Turtle()
y = t.Turtle()
w = t.Turtle()
m = t.Turtle()

p1 = inputPoints() #getting the input from inputPoints.py

z.pu()
y.pu()
w.pu()
m.pu()
t.pu()
s = t.Screen() # Once done, turtle screen emerges
# Hiding the turtles
z.hideturtle()
y.hideturtle()
w.hideturtle()
m.hideturtle()
t.hideturtle()
#speed of turtle
z.speed(0)
y.speed(0)
w.speed(0)
m.speed()

def draw(): #drawing of points of points from the file and inputting coordinates manually
    z.pu()
    y.pu()
    w.pu()
    y.goto(p1[0][0],p1[0][1]) #goes to first coordinate without drawing line
    for i in p1:
        y.goto(i[0], i[1])
        y.pd()
        y.write(str(round(i[0],1)) + ", " + str(round(i[1],1))) # write the cursor point coordinate
    y.goto(p1[0][0],p1[0][1]) #goes back to first coordinate
    y.pu()

def draw2(polygon_no): #drawing of points of functions
    z.pu()
    y.pu()
    w.pu()
    if polygon_no == 1:
        y.goto(p2[0][0],p2[0][1])
        for i in p2:
            y.goto(i[0], i[1])
            y.pd()
            #rounding off of coordinates
            y.write(str(round(i[0],1)) + ", " + str(round(i[1],1))) # write the cursor point coordinate
        y.goto(p2[0][0],p2[0][1])
        y.pu()
    elif polygon_no == 2:
        w.goto(pnew[0][0],pnew[0][1])
        for i in pnew:
            w.goto(i[0], i[1])
            w.pd()
            w.write(str(round(i[0],1)) + ", " + str(round(i[1],1))) # write the cursor point coordinate
        w.goto(pnew[0][0],pnew[0][1])
        w.pu()
    
#drawing grid on turtle screen
def grid():
    z.pu()
    z.goto(-600,325)
    for a in range(30):
        for b in range(50):
            z.dot(3,"black")
            z.forward(20)
        z.back(1000)
        z.right(90)
        z.forward(20)
        z.left(90)
    z.pu()

grid() #calling out drawing of dot grid function

#storing of values of p1 inside values.txt
doc = open("values.txt", "w") 
for coordinates in p1: #stores every coordinate at every line
    string = str(coordinates[0]) + "," + str(coordinates[1]) 
    print(string, file = doc )
doc.close()


#Drawing of the GUI
def rectangle(x,y,name = "empty"):
    z.pu()
    z.goto(x,y)
    z.pd()
    z.forward(125) # Forward turtle by s units
    z.left(90) # Turn turtle by 90 degree
    z.forward(50) # Forward turtle by s units
    z.left(90) # Turn turtle by 90 degree
    z.forward(125) # Forward turtle by s units
    z.left(90) # Turn turtle by 90 degree
    z.forward(50) # Forward turtle by s units
    z.left(90) # Turn turtle by 90 degree
    z.pu()
    z.goto(x+25, y+20)# going inside the rectangle
    z.write(name, font =("Verdana", 7, "normal")) #writing name of the function
    z.pu()

rectangle(425,300,"Right w/o dup") #Right w/out duplicate
rectangle(600,300,"Right w dup") #Right w duplicate

rectangle(425,225, "Left w/o dup") #Left w/out duplicate
rectangle(600,225, "Left w dup") #Left w duplicate

rectangle(425,150, "Up w/o dup") #Up w/out duplicate
rectangle(600,150, "Up w dup") #Up w duplicate

rectangle(425,75, "Down w/o dup") #Down w/out duplicate
rectangle(600,75, "Down w dup") #Down w duplicate

rectangle(425,0, "Rotate w/o dup") #Rotate w/out duplicate
rectangle(600,0, "Rotate w dup") #Rotate w duplicate

rectangle(425,-75, "Scaleup w/o dup") #Scaleup w/out duplicate
rectangle(600,-75, "Scaleup w dup") #Scaleup w duplicate

rectangle(425,-150, "Scaledown w/o dup") #Scaledown w/out duplicate
rectangle(600,-150, "Scaledown w dup") #Scaledown w duplicate

rectangle(425,-225, "Perimeter") #Perimeter
rectangle(600,-225, "Area") #Area

rectangle(425,-300, "Outline of shape") #Change color of outline of shape #use text input
rectangle(600,-300, "Fill shape") #Fill shape color #use text input

rectangle(425,-375, "Change Vertex") #Change vertex of shape
rectangle(600,-375, "Add Polygon") #Fill shape color #use text input

rectangle(250,-375, "Determine point") #determine if point is in the polygon
rectangle(75,-375, "Change polygon no") #change polygon number to modify

p2 = p1[:] #copies p1 which is original list so that changes to list can be made without altering original list
polygon_no = 1 #polygon number for working with new polygon
pnew = [] #newlist for new polygon

#defining all the functions for polygon manipulation and functions, with and without duplicates
def right_wo_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[0] += 10 #shifting by 10 units
    elif polygon_no == 2:
        for points in pnew:
            points[0] += 10       
    y.clear()
    draw2(polygon_no)
    
def right_w_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[0] += 10 #shifting by 10 units
    elif polygon_no == 2:
        for points in pnew:
            points[0] += 10   
    draw2(polygon_no)
    
def left_wo_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[0] -= 10 #shifting by 10 units
    elif polygon_no == 2:
        for points in pnew:
            points[0] -= 10   
    y.clear()
    draw2(polygon_no)
    
def left_w_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[0] -= 10 #shifting by 10 units
    elif polygon_no == 2:
        for points in pnew:
            points[0] -= 10   
    draw2(polygon_no)
    
def up_wo_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[1] += 10 #shifting by 10 units
    elif polygon_no == 2:
        for points in pnew:
            points[1] += 10   
    y.clear()
    draw2(polygon_no)
    
def up_w_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[1] += 10 #shifting by 10 units
    elif polygon_no == 2:
        for points in pnew:
            points[1] += 10   
    draw2(polygon_no)
    
def down_wo_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[1] -= 10 #shifting by 10 units
    elif polygon_no == 2:
        for points in pnew:
            points[1] -= 10   
    y.clear()
    draw2(polygon_no)
    
def down_w_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[1] -= 10 #shifting by 10 units
    elif polygon_no == 2:
        for points in pnew:
            points[1] -= 10   
    draw2(polygon_no)
    
def rotate_wo_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            temp1 = points[0]
            temp2 = points[1]
            points[0] = temp1 * math.cos(pi/4) - temp2 * math.sin(pi/4) #rotating of polygon by 45 degrees about origin
            points[1] = temp2 * math.cos(pi/4) + temp1 * math.sin(pi/4)
    elif polygon_no == 2:
        for points in pnew:
            temp1 = points[0]
            temp2 = points[1]
            points[0] = temp1 * math.cos(pi/4) - temp2 * math.sin(pi/4)#rotating of polygon by 45 degrees about origin
            points[1] = temp2 * math.cos(pi/4) + temp1 * math.sin(pi/4)
    y.clear()
    draw2(polygon_no)
    
def rotate_w_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            temp1 = points[0]
            temp2 = points[1]
            points[0] = temp1 * math.cos(pi/4) - temp2 * math.sin(pi/4)#rotating of polygon by 45 degrees about origin
            points[1] = temp2 * math.cos(pi/4) + temp1 * math.sin(pi/4)
    elif polygon_no == 2:
        for points in pnew:
            temp1 = points[0]
            temp2 = points[1]
            points[0] = temp1 * math.cos(pi/4) - temp2 * math.sin(pi/4)#rotating of polygon by 45 degrees about origin
            points[1] = temp2 * math.cos(pi/4) + temp1 * math.sin(pi/4)
    draw2(polygon_no)
    
def scaledown_wo_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[0] = points[0]/2 #scaling down by half
            points[1] = points[1]/2
    elif polygon_no == 2:
        for points in pnew:
            points[0] = points[0]/2
            points[1] = points[1]/2
    y.clear()
    draw2(polygon_no)
    
def scaledown_w_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[0] = points[0]/2 #scaling down by half
            points[1] = points[1]/2
    elif polygon_no == 2:
        for points in pnew:
            points[0] = points[0]/2
            points[1] = points[1]/2
    draw2(polygon_no)
    
def scaleup_wo_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[0] = points[0]*2 #scaling by twice the size
            points[1] = points[1]*2
    elif polygon_no == 2:
        for points in pnew:
            points[0] = points[0]*2
            points[1] = points[1]*2
    y.clear()
    draw2(polygon_no)
    
def scaleup_w_dup(polygon_no):
    if polygon_no == 1:
        for points in p2:
            points[0] = points[0]*2 #scaling by twice the size
            points[1] = points[1]*2
    elif polygon_no == 2:
        for points in pnew:
            points[0] = points[0]*2
            points[1] = points[1]*2
    draw2(polygon_no)

#perimeter 
def perimeter(polygon_no):
    perimeter = 0
    if polygon_no == 1:
        for pt in range(len(p2)-1):
            perimeter += math.sqrt((p2[pt + 1][0]- p2[pt][0])**2 + (p2[pt + 1][1]- p2[pt][1])**2) #pythagoras thm
        perimeter += math.sqrt((p2[pt][0]- p2[0][0])**2 + (p2[pt + 1][1]- p2[0][1])**2)
    elif polygon_no == 2:
        for pt in range(len(pnew)-1):
            perimeter += math.sqrt((pnew[pt + 1][0]- pnew[pt][0])**2 + (pnew[pt + 1][1]- pnew[pt][1])**2)
        perimeter += math.sqrt((pnew[pt][0]- pnew[0][0])**2 + (pnew[pt + 1][1]- pnew[0][1])**2)
    w.pu()
    w.goto(-600,-350)
    w.write("perimeter = {:.2f}".format(perimeter), font =("Verdana", 12, "normal"))

    
def area(polygon_no):
    total_area = 0
    if polygon_no == 1:        
        for number in range(2, len(p2) - 1): #using formula given in assigment handout
            total_area += p2[0][0] * p2[number][1] - p2[0][1] * p2[number][0]
    elif polygon_no == 2:
        for number in range(2, len(p2) - 1):
            total_area += pnew[0][0] * pnew[number][1] - pnew[0][1] * pnew[number][0]
    w.pu()
    w.goto(-600,-325)
    w.write("area = {:.2f}".format(total_area), font =("Verdana", 12, "normal"))

linecolorno = 0
def line_color(polygon_no):
    linecolor = ["black", "red", "blue", "green"]
    y.clear()
    global linecolorno
    linecolorno += 1 # counter for list of line color
    if linecolorno == 4:
        linecolorno = 0
    y.pencolor(linecolor[linecolorno]) #change color of the pens
    w.pencolor(linecolor[linecolorno])
    draw2(polygon_no)

colorcounter = 0    
def fill(polygon_no):
    colorlist = ["black", "red", "blue", "green"]
    global colorcounter
    colorcounter += 1
    if colorcounter == 4:
        colorcounter = 0
    y.clear()
    y.fillcolor(colorlist[colorcounter])
    w.fillcolor(colorlist[colorcounter])   
    y.beginfill()
    y.goto(p2[0][0],p2[0][1])
    for i in p2:
        y.goto(i[0], i[1])
        y.pd()
        #rounding off of coordinates
        y.write(str(round(i[0],1)) + ", " + str(round(i[1],1))) # write the cursor point coordinate
    y.goto(p2[0][0],p2[0][1])
    y.pu()
    y.endfill()


def amend(polygon_no):
    coordinatenumber = s.textinput("Amendment" , "Please input the index of the coordinate(starting with 1), followed by the two coordinates (eg. 1,200,200):")
    try:
        temp1 = coordinatenumber.split(",") #split code into different chunks separated by commas
        #check if input is in terms of numbers
        temp1[0] = int(temp1[0])
        temp1[1] = float(temp1[1])
        temp1[2] = float(temp1[2])
        p2[temp1][0][0] = temp1[1]
        p2[temp1][0][1] = temp1[2]
        y.clear()
        draw(p2)
    except IndexError: #if unable to split the input, then will form index error because b[1] wont exist
        print("Please input a proper coordinate")

def add():
    def endshape(): #define function space bar that draws line from last click to the first click to end the shape
        t.goto(pnew[0][0], pnew[0][1])
    def line2(x,y):
        m.goto(x,y)
        m.pd()
        m.write(str(x) + ", " + str(y)) # write the cursor point coordinate
        pnew.append([x, y])  # add the point to the polygon list data
        s.onkey(endshape,"e") #if spacebar is clicked, goes back to first coordinate
        s.listen()
    m.pu()
    s.onclick(line2)


def inpolygon(polygon_no):
    coord_to_test = s.textinput("In Polygon" , "Please input the index of the coordinate(eg.200,200):")
    coord = []
    temp3 = coord_to_test.split(",") #split code into different chunks separated by commas
    coord.append(int(temp3[0]))
    coord.append(int(temp3[1]))# add the point to the polygon list data]

#referenced     
    def onSegment(p,q,r): # Given three collinear points p,q and r
        if ((q[0] <= max(p[0], r[0])) & (q[0] >= min(p[0], r[0])) & (q[1] <= max(p[1], r[1])) & (q[1] >= min(p[1], r[1]))):
            return True
        return False

    def orientation(p,q,r): 
        val = (((q[1] - p[1])*(r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))) 
        #slope of first line pq = (q[1] - p[1])/(q[0] - p[0]), second slope is (r[1] - q[1])/(r[0] - q[0])
        #compare the two slopes using val, either clockwise or anticlockwise  or collinear
        if val == 0:
            return 0 # Collinear
        if val > 0:
            return 1 # Clockwise
        else:
            return 2 # counterclock

    def doIntersect(p1,q1,p2,q2):
    # Find the four orientations needed for 
        # general and special cases
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)
        # General case
        if (o1 != o2) and (o3 != o4):
            return True
        
        # Special Cases
        # p1, q1 and p2 are collinear and
        # p2 lies on segment p1q1
        if (o1 == 0) and (onSegment(p1, p2, q1)):
            return True

        # p1, q1 and p2 are collinear and
        # q2 lies on segment p1q1
        if (o2 == 0) and (onSegment(p1, q2, q1)):
            return True

        # p2, q2 and p1 are collinear and
        # p1 lies on segment p2q2
        if (o3 == 0) and (onSegment(p2, p1, q2)):
            return True

        # p2, q2 and q1 are collinear and
        # q1 lies on segment p2q2
        if (o4 == 0) and (onSegment(p2, q1, q2)):
            return True

        return False
    # Returns true if the point p lies 
    # inside the polygon[] with n vertices
    def is_inside_polygon(points, coord):

        n = len(points)
        
        # There must be at least 3 vertices
        # in polygon
        if n < 3:
            return False
            
        # Create a point for line segment
        # from p to infinite
        extreme = (1000, coord[1])
        count = i = 0
        
        while True:
            next = (i + 1) % n
            
            # Check if the line segment from 'p' to 
            # 'extreme' intersects with the line 
            # segment from 'polygon[i]' to 'polygon[next]'
            if (doIntersect(points[i],
                            points[next],
                            coord, extreme)):
                                
                # If the point 'p' is collinear with line 
                # segment 'i-next', then check if it lies 
                # on segment. If it lies, return true, otherwise false
                if orientation(points[i], coord,
                            points[next]) == 0:
                    return onSegment(points[i],coord,
                                    points[next])
                                    
                count += 1
                
            i = next
            if (i == 0):
                break
        
        # Return true if count is odd, false otherwise
        return (count % 2 == 1)
    
    if (is_inside_polygon(p1,coord)):
        w.pu()
        w.goto(-400,-325)
        w.write("Point is in the Polygon", font =("Verdana", 12, "normal"))
    else:
        w.pu()
        w.goto(-400,-325)
        w.write("Point is not in the Polygon", font =("Verdana", 12, "normal"))


#listening to clicks on the boxes
def function(x,y):
    if  425 <= x <= 550 and 300<= y <= 350: #right_wo_dup
        right_wo_dup(polygon_no)
    elif 600 <= x <= 725 and 300<= y <= 350: #right_w_dup
        right_w_dup(polygon_no)
    elif 425 <= x <= 550 and 225<= y <= 275: #left_wo_dup
        left_wo_dup(polygon_no)
    elif 600 <= x <= 725 and 225<= y <= 275: #left_w_dup
        left_w_dup(polygon_no)
    elif 425 <= x <= 550 and 150<= y <= 200: #up_wo_dup
        up_wo_dup(polygon_no)
    elif 600 <= x <= 725 and 150<= y <= 200: #up_w_dup
        up_w_dup(polygon_no)
    elif 425 <= x <= 550 and 75<= y <= 125: #down_wo_dup
        down_wo_dup(polygon_no)
    elif 600 <= x <= 725 and 75<= y <= 125: #down_w_dup
        down_w_dup(polygon_no)
    elif 425 <= x <= 550 and 0<= y <= 50: #rotate_wo_dup
        rotate_wo_dup(polygon_no)
    elif 600 <= x <= 725 and 0<= y <= 50: #rotate_w_dup
        rotate_w_dup(polygon_no)
    elif 425 <= x <= 550 and -75<= y <= -25: #scaleup_wo_dup
        scaleup_wo_dup(polygon_no)
    elif 600 <= x <= 725 and -75<= y <= -25: #scaleup_w_dup
        scaleup_w_dup(polygon_no)
    elif 425 <= x <= 550 and -150<= y <= -100: #scaledown_wo_dup
        scaledown_wo_dup(polygon_no)
    elif 600 <= x <= 725 and -150<= y <= -100: #scaledown_w_dup
        scaledown_w_dup(polygon_no)
    elif 425 <= x <= 550 and -225<= y <= -175: #perimeter
        perimeter(polygon_no)
    elif 600 <= x <= 725 and -225<= y <= -175: #area
        area(polygon_no)
    elif 425 <= x <= 550 and -300<= y <= -250: #color
        line_color(polygon_no)
    elif 600 <= x <= 725 and -300<= y <= -250: #fill
        fill(polygon_no)
    elif 425 <= x <= 550 and -375<= y <= -325: #amend vertex
        amend(polygon_no)
    elif 600 <= x <= 725 and -375<= y <= -325: #add polygon
        add()
    elif 250 <= x <= 375 and -375<= y <= -325: #determine if inside polygon
        inpolygon(polygon_no)
##  elif 75 <= x <= 200 and -375<= y <= -325: #determine polygon number 
##        polygon_no = 2
        
            
z.pu()
y.pu()
w.pu()
m.pu()
t.pu()
s.onclick(function)
s.listen()

#Drawing of points    
draw()

# detect if lines in polygon is self-intersecting
for every_coord in range(len(p1)):
    for every_coord2 in range(len(p1)):
        if doIntersect(p1[every_coord],p1[every_coord + 1], p1[every_coord2],p1[every_coord2 + 1]) == False:
            turtle.bye()
            print("Coordinates intersect! Please try again!")
        





