# initial setup of stations in the subway map
stations = []
harvard_square = ("Harvard Square", 'red', None)
stations.append(harvard_square)
central_square = ("Central Square", 'red', None)
stations.append(central_square)
kendall_square = ("Kendall Square", 'red', None)
stations.append(kendall_square)
south_station = ("South Station", 'red', None)
stations.append(south_station)
park_street = ("Park Street", 'red', 'green')
stations.append(park_street)
boston_u = ("Boston U", 'green', None)
stations.append(boston_u)
copley_square = ("Copley Square", 'green', None)
stations.append(copley_square)
washington = ("Washington", 'red', 'orange')
stations.append(washington)
north_station = ("North Station", 'green', None)
stations.append(north_station)
haymarket = ("Haymarket", 'green', None)
stations.append(haymarket)
government_center = ("Government Center", 'green', 'blue')
stations.append(government_center)
wood_island = ("Wood Island", 'blue', None)
stations.append(wood_island)
airport = ("Airport", 'blue', None)
stations.append(airport)
aquarium = ("Aquarium", 'blue', None)
stations.append(aquarium)
state = ("State", 'blue', 'orange')
stations.append(state)

# test print for the stations and their tuples
#for station in stations:
#    print(station[0])

# a list containing the path to take
path = []
# a list that contains the intersections calculated for a given state if needed
intersections = []

# solves the path based on a set of if statements
def SolvePath(currentState, goalState):
    intersections.clear()
    path.append(currentState)
    # if the current state and the goal state are the same
    if currentState[0] == goalState[0]:
        PrintPath(path)

    # if the current state and the goal state are ont he same line
    elif goalState[1] == currentState[1] or goalState[1] == currentState[2]:
        nextState = goalState
        SolvePath(nextState, goalState)

    # if the current state and the goal state are not on the same line
    elif goalState[1] != currentState[1]:
        # calculate the intersections for a given state
        for station in stations:
            if station[1] == currentState[1] and station[2] is not None:
                 intersections.append(station)
            elif station[2] == currentState[1]:
                 intersections.append(station)
        # test print for intersections
        #for intersection in intersections:
        #    print(intersection)
        # the next state is the first intersection in the list
        nextState = intersections.pop(0)
        # test print
        # print(nextState)
        SolvePath(nextState, goalState)

# a method to print the final pathway
def PrintPath(pathway):
    for step in pathway:
        print(step[0])

# driver
SolvePath(wood_island, harvard_square)
