
def get_route_length(current_route, network):
    route_length = network[current_route[-1]][current_route[0]]['cost']
    for index in range(len(current_route)-1):
        city1 = current_route[index]
        city2 = current_route[index+1]
        route_length += network[city1][city2]['cost']

    return route_length

# read from file
def read_graph_from_file(filename):
    routes = []
    with open(filename, 'r') as file:
        cities_no = int(file.readline())
        for i in range(cities_no):
            city_routes_string = file.readline().strip().split(',')
            city_routes = build_route_structure(city_routes_string)
            routes.append(city_routes)
    return routes


# build routes structure
def build_route_structure(string_routes):
    final_routes = []
    for city_index, route_cost in enumerate(string_routes):
        city_details = {'city': city_index + 1, 'cost': int(route_cost)}
        final_routes.append(city_details)
    return final_routes


# write/append to file
def result_to_file(access_mode, output_file, no_of_cities, cities_order, total_cost):
    with open(output_file, access_mode) as output:
        output.write(str(no_of_cities) + '\n')
        output.write(str(cities_order)[1:-1] + '\n')
        output.write(str(total_cost) + '\n')
