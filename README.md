# wonkavator

# Overview:
We will simulate a building in which the Wonkavator will move around. The building will be 
represented by a 3D grid, where each coordinate in the grid represents a room. The Wonkavator 
can travel from room to room by moving at most 1 unit in any direction. For example, it could 
move from point (2, 3, 4) to point (2, 4, 5), by making a movement of (0, 1, 1). However, it 
is illegal to make a move from (1, 1, 1) to (3, 1, 1), as we can move a maximum of 1, not 2, 
in any direction. A move of (0, 0, 0) (i.e., staying in place) is also invalid. Further, it is 
invalid to move beyond the bounds of the grid (i.e., out of the building). If the Wonkavator 
is at coordinate (5, 5,4), and the grid is of size 6x6x6, then it is invalid to move in the 
direction (1, 0, 0), as that would bring the Wonkavator out of the grid.

# Background:
There will be three classes defined: Person, Factory and Wonkavator:

  - The Person class defines a person inside the building. At the start of the simulation, each
    Person will be located at one particular (x, y, z) coordinate in the grid, and will want to
    travel to some other (x, y, z) coordinate. The Person class contains four attributes: the
    person's name, their current position in the grid (represented as a Point3D object), their
    destination position in the grid (represented as a Point3D object), and finally a boolean
    variable indicating whether or not they have arrived at their destination yet.

  - The Wonkavator class contains methods to move the Wonkavator and maintain the list of people
    currently inside. The Wonkavator must travel to each person's (x, y, z) coordinate, moving by
    at most 1 in any dimension at a time (as described above). After picking up a person, it must
    deliver them to their destination (x, y, z) coordinate. (Note: The Wonka-vator doesn't have to
    deliver a person right after picking them up; it could pick up multiple people before delivering
    all of them to their destinations.) Once a person has reached their destination, they remain
    there for the rest of the simulation. The Wonkavator class contains three attributes: its current
    position in the grid (represented as a Point3D object, the size of the factory (represented as a
    Point3D object), and a list of the people currently in the Wonkavator.

  - ﻿﻿The Factory class contains methods to run the simulation and display it to the screen. It also
    contains four attributes: the size of the factory (a Point3D object), a list of the people in the
    simulation (i.e., a list of Person objects), one object of type Wonkavator for the actual elevator,
    and finally an attribute relating to the Matplotlib visualization.

# Instructions:

1. _init_ method of Person class
 
Parameters: In addition to self, a string name, Point3D object cur-pos and Point3D object dst_pos.

What it should do: 

  - Create four attributes: name, cur_pos, dst_pos and arrived. The first three 
    attributes should be assigned the values of the respective parameters, while the arrived attribute 
    should be set to False.

2. run method of Factory class

Parameters: No parameters (just self).

What it should do: 

  - This method is the main loop for the simulation. It checks to see if the elevator 
    is currently in a room where there are people who want to enter the elevator, and/or if there are 
    people in the elevator whose destination point is the current room and who thus want to leave the 
    elevator.

  - If there is a person(s) who are in the same room as the elevator and need to be picked up, then, for 
    each such person, the person_enters method of the elevator attribute should be called, with the person 
    passed as argument to the method. However, make sure that the person does need to be picked up and has 
    not already arrived at their destination room (you can check the arrived method of the person - if it 
    is True, then they should not be picked up as they have already arrived).

  - If there is a person(s) who are in the elevator and whose destination is the current room, and thus need 
    to be dropped off in the room, the person_leaves method of the elevator attribute should be called, 
    with the person passed as argument to the method.
  
  - Finally, the method should call the move method of the elevator attribute, and pass the list of people 
    (self .people) as argument. (This line is already done for you.)

3. choose_direction method of Wonkavator class
   
Parameters: In addition to self, people: a list of Person objects

What it should do: 

  - This method tells the elevator in which direction to move, by returning a Point3D object with the
    direction to move in each dimension. The elevator can only move a maximum of 1 unit in any dimension,
    so each component of the direction must be either -1, 0, or 1. (Note that a direction of (0, 0, 0)
    is invalid as the elevator cannot stay in the same place, but a direction of (1, 1, -1) is fine.)

  - There is no constraint in how this method should be designed, but the simulation must end with all
    people taken to their destinations. Thus, the method should return a direction such that it moves
    closer either to picking up a person or dropping off a person, so that in the end, the simulation
    can finish.

  - Given two Point3D objects x and y, calling x. get_direction vector (y) will return a direction vector
  - of one unit in each dimension from x moving towards y.)
