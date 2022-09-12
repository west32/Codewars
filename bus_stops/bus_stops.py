def number(bus_stops):


    # inside = 0
    # left = 0
    # for element in bus_stops:
    #     inside += element[0]
    #     left += element[1]
    #
    # return inside - left
    return sum([stop[0] - stop[1] for stop in bus_stops])
