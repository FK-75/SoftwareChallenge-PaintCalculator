### Input Values 

length,width,height = [int(x) for x in (input("Type the length, width and height of the room in meters separated by commas i.e. 5,5,5 :").split(","))]

### Area of the Floor 
areaOfFloor = round((length * width),2)


### Amount of paint required to paint the walls

## 1 litre = 12 m^2 of coverage
litresOfPaint = round(((length*height + width*height)/6),2) ## Assuming room is rectangular
# if assuming a room is rectangular, total area of walls = 2*(length*height + width*height)
# and since 1l = 12m^2 total amount of paint for walls = total area of walls/12 = 2*(length*height + width*height)/12 = (length*height + width*height)/6 


## Volume of the room
volumeOfRoom = round((length*width*height),2)

# f string for printing return values
print(f'The area of the floor is {areaOfFloor}m^2, it would require {litresOfPaint}L of paint to paint the walls, the volume of the room is {volumeOfRoom}m^3')