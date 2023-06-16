# MA1008-Mini-Project

# This is a project for MA1008 - Introduction to Computational Thinking #

You are to write a program that can create, store, retrieve and manipulate polygons. Your program 
should have the following capabilities:

## i. Polygon Creation ## 
Create a polygon, store its data in a file, and retrieve it when needed. A polygon is represented by its vertices.
You need to provide two methods of input:

a. Type in their coordinates or 

b. Generate them by mouse clicks in the graphics display.

Both capabilities need to be provided in your program. You would need to setup the data 
structure for your polygon first. We exclude self-intersecting polygons from this project. Hence 
your program should raise an error and prevent the creation of a self-intersecting polygon. 

## ii. Polygon Edges ##
A polygon can have as many edges as the user desires. You need to allow two types of edges:

a. Straight. A straight edge is defined by two adjacent polygon vertices. 

b. Curved. Curved edges are discussed in Appendix 1.

## iii. Displaying a Polygon ##
Display the polygon graphically. There are two display options:

a. the outline of the polygon and 

b. the interior filled with a colour.

A display may use one or both the options. The user should be able to choose the colour for 
both the options. You may display multiple different polygons at the same time, each with its 
own display options.

## iv. Manipulating a polygon ##
There are many possible manipulations. You need to provide the following five:

a. Modify the polygon by deleting an existing vertex or inserting a new one. Then display the 
outcome.

b. Move the polygon by a specific distance in a specific direction. (Panning)

c. Rotate the polygon by a specific angle about a specific point.

d. Scale the polygon up or down by a specific factor.

e. Produce multiple copies of the polygon, either linearly or by rotational about a point, with 
or without scaling.

## v. Analytical Tools using a Polygon ##
There are numerous useful things one can do with a polygon. Provide these in your program:

a. Find the perimeter length of the polygon.

b. Find the area of the polygon.

c. Determine if a given point is inside, outside or on the boundary of the polygon. 

d. Select a polygon by pointing to it with the mouse cursor, and then manipulate it. The 
selection can be done using the capability of Item c above or by pointing to an edge of the 
polygon, which means your program needs to know if the cursor is at an edge. This 
capability is required when you have multiple polygons displayed and need to manipulate 
individual ones.

## vi. File Input and Output ## 
Provide a data file that stores polygons that you have created. Hence your program should have 
two means of input:

a. The method described above in Item i Polygon Creation.

b. Reading in from file
