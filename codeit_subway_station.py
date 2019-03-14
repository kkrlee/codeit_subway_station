from collections import deque

# class of Station
class Station:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_connection(self, another_station):
        self.neighbors.append(another_station)
        another_station.neighbors.append(self)


# Breadth-First Search algorithms
def bfs(start, goal):
    # variable definition
    previous = {}
    queue = deque()
    current = None

    # beginning setting
    previous[start] = None
    queue.append(start)

    # search
    while len(queue) > 0 and current != goal:
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in previous.keys():
                queue.append(neighbor)
                previous[neighbor] = current

    # making and return if there are ways
    if current == goal:
        path = [goal]
        x = goal

        while previous[x] != None:
            x = previous[x]
            path.append(x)

        return path

    # not making and return if there are not ways
    return None


# read file
stations = {}
in_file = open("stations.txt", "rt", encoding='utf8')

for line in in_file:
    previous_station = None
    data = line.strip().split("-")

    for name in data:
        station_name = name.strip()
        if station_name not in stations.keys():
            current_station = Station(station_name)
            stations[station_name] = current_station
        else:
            current_station = stations[station_name]

        if previous_station != None:
            current_station.add_connection(previous_station)

        previous_station = current_station

in_file.close()


# test
start_name = "이태원"
goal_name = "잠원"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)
