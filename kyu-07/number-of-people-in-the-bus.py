def number(bus_stops):
    result = 0
    for i in bus_stops:
        result += i[0]
        result -= i[1]
    return result


def number_on_bus(bus_stops):
    return sum(i[0] - i[1] for i in bus_stops)
