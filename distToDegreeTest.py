import math 

num_links = 4
link_length = 70
pinion_diameter = 16

def distToDegree(distance):
    '''
    Convert a distance that the arm needs to move, to the associated degs to turn the stepper motor
    '''
    distance = 200
    print("distance: ", distance)
    distance_per_link = distance / num_links
    print("distance_per_link", distance_per_link)
    horizontal_distance = math.cos(math.asin(distance_per_link / link_length)) * link_length
    print("horizontal_distance", horizontal_distance)
    deg = horizontal_distance / (math.pi * pinion_diameter)
    if(deg > 400):
        print("Distance to big: ", deg)
        return 0
    print("Degree: ", deg)
    return deg

while True:
    dist = int(input("New Dist: "))

    deg = distToDegree(dist)

    print("Degrees are", deg)