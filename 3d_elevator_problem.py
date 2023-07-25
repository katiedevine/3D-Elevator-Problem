# 3d_elevator_problem

import math
from random import randint
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

plt.ion()
#enable interactive mode (continue graphing without having to close the window)

plt.show()
#show the plot


def sign(x):
#Return the sign of x (0 if x is 0).
    
    if x > 0:
    #x positive
        return 1
    
    elif x < 0:
    #x negative
        return -1
    
    else:
    #x zero
        return 0


class Point3D():
    
    def __init__(self, x, y, z):
    #class constructor
        
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    
    def __eq__(self, other):
    #comparison
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __str__(self):
    #string representation
        return '<{}, {}, {}>'.format(self.x, self.y, self.z)
    
    def add(self, other):
    #add two points together
        return Point3D(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def distance(self, other):
    #get distance between two points
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
    
    def get_direction_vector(self, other):
        #Return a vecotr of 1, 0 or -1 in each dimension corresponding to
        #the direction you would have to move from the self point to get to the other point.
        return Point3D(sign(other.x-self.x), sign(other.y-self.y), sign(other.z-self.z))
    
    def aslist(self):
    #Return the Point2D object as a list of three numbers.
        return [self.x, self.y, self.z]

def get_random_point(x0, x1, y0, y1, z0, z1):
#return a Point3D object with random coordinates within the given x,y,z intervals.
    return Point3D(randint(x0, x1), randint(y0, y1), randint(z0, z1))

class Person:
#defining the class constructor 'Person'

    def __init__(self, name, cur_pos, dst_pos):
    #creating a new attribute
    
        self.name = name
        self.cur_pos = cur_pos
        self.dst_pos = dst_pos
        self.arrived = False
        #assigning default values

    def arrive_at_destination(self):
        self.cur_pos = self.dst_pos
        self.arrived = True
        
    def __str__(self):
    #string representation
        return "Name:" + self.name + "; cur: " + str(self.cur_pos) + "; dst:" + str(self.dst_pos)


class Factory:
    
    def __init__(self, factory_size, people, elevator):
    #class constructor
        self.factory_size = factory_size
        self.people = people
        self.elevator = elevator
        
        self.axes = plt.axes(projection='3d')
    
    def run(self):
        
        for person in self.people:

            #Check if people want to enter the elevator
            if self.elevator.cur_pos == person.cur_pos and person.arrived == False:
                self.elevator.person_enters(person)
                #if the person and the elevator are in the same position and they haven't arrived at their destination, the person enters the elevator
         
            #Check if people want to leave the elevator
            elif self.elevator.cur_pos == person.dst_pos and person in self.elevator.people_in_elevator:
                self.elevator.person_leaves(person)
                #if the person is in the elevator and their current position is their destination, the person will leave the elevator
            
        #Move the elevator.
        if not self.is_finished():
            self.elevator.move(self.people)
    
    def show(self):
    #display the grid
        
        self.axes.clear()
        #clear the previous window contents
        
        #set the axis bounds
        self.axes.set_xlim(0, factory_size.x)
        self.axes.set_ylim(0, factory_size.y)
        self.axes.set_zlim(0, factory_size.z)
        self.axes.set_xticks(list(range(factory_size.x+1)))
        self.axes.set_yticks(list(range(factory_size.y+1)))
        self.axes.set_zticks(list(range(factory_size.z+1)))
        
        #show a blue dot for each person not yet in the elevator / not yet arrived at their destination
        xs, ys, zs = [], [], []
        for person in self.people:
            if not person.arrived and person not in self.elevator.people_in_elevator:
                xs.append(person.cur_pos.x)
                ys.append(person.cur_pos.y)
                zs.append(person.cur_pos.z)
        self.axes.scatter3D(xs, ys, zs, color='blue')
        
        #show a red dot for the destinations of the people currently in the elevator
        edxs, edys, edzs = [], [], []
        for person in self.people:
            if person in self.elevator.people_in_elevator:
                edxs.append(person.dst_pos.x)
                edys.append(person.dst_pos.y)
                edzs.append(person.dst_pos.z)
        self.axes.scatter3D(edxs, edys, edzs, color='red')
        
        #show a green dot for the elevator itself
        self.axes.scatter3D([self.elevator.cur_pos.x], [self.elevator.cur_pos.y], [self.elevator.cur_pos.z], color='green')
        
        plt.draw()
        plt.pause(0.5)
    
    def is_finished(self):
        return all(person.arrived for person in self.people)


class Wonkavator:
    def __init__(self, factory_size):
    #class constructor
        self.cur_pos = Point3D(0, 0, 0)
        self.factory_size = factory_size
        self.people_in_elevator = []
        #the list of people currently in the elevator
        
    def move(self, people):
    #move the elevator
        #get the direction in which to move      
        direction = self.choose_direction(people)
        
        #check if the direction is correct
        if any(not isinstance(d, int) for d in direction.aslist()):
            raise ValueError("Direction values must be integers.")
        if any(abs(d) > 1 for d in direction.aslist()):
            raise ValueError("Directions can only be 0 or 1 in any dimension.")
        if all(d == 0 for d in direction.aslist()):
            raise ValueError("The elevator cannot stay still (direction is 0 in all dimensions).")
        if any(d < 0 or d > s for d, s in zip(self.cur_pos.add(direction).aslist(), self.factory_size.aslist())):
            raise ValueError("The elevator cannot move outside the bounds of the grid.")
        
        #move the elevator in the correct direction
        self.cur_pos = self.cur_pos.add(direction)
        
    def choose_direction(self, people):
    #Return the direction in which to move, as a Point3D object.
        
        for person in people:
        #iterate over every person in the list of people
            
            if person in self.people_in_elevator:
            #if the person is in the elevator
                return self.cur_pos.get_direction_vector(person.dst_pos)
                #return the direction between the person's destination and their current position
            
            elif person.arrived == False:
            #if the person hasn't arrived
                return self.cur_pos.get_direction_vector(person.cur_pos)
                #return the direction between the person's current position and the elevator
            
            else:
            #if the person has arrived, do not do anything and continue the for loop
                continue
     
    def person_enters(self, person):
    #person arrives in elevator
        if person.arrived:
            raise Exception("A person can only enter the elevator if they have not yet reached their destination.")
        
        self.people_in_elevator.append(person)
        #add them to the list
    
    def person_leaves(self, person):
    #person departs elevator
        if person.dst_pos != elevator.cur_pos:
            raise Exception("A person can only leave the elevator if the elevator has reached their destination point.")
        
        person.arrive_at_destination()
        #let the person know they have arrived
        self.people_in_elevator.remove(person)
        #remove them from the list


if __name__ == '__main__':    
    factory_size = Point3D(5, 5, 5)
    
    #create the people objects
    people = []
    for name in ["Candice", "Arnav", "Belle", "Cecily", "Faizah", "Nabila", "Tariq", "Benn"]:
        cur = get_random_point(0, factory_size.x-1, 0, factory_size.y-1, 0, factory_size.z-1)
        dst = get_random_point(0, factory_size.x-1, 0, factory_size.y-1, 0, factory_size.z-1)
        people.append(Person(name, cur, dst))
    
    #create the elevator
    elevator = Wonkavator(factory_size)
    
    #create the factory
    factory = Factory(factory_size, people, elevator)
    
    while True:
        factory.run()
        factory.show()
        
        #check if everyone has arrived at their destinations
        if factory.is_finished():
            break
    
    print("Everyone has arrived.")
