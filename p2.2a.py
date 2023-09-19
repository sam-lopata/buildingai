portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    global smallest
    global bestroute
    # write the recursive function here
    # remember to calculate the emissions of the route as the recursion ends
    # and keep track of the route with the lowest emissions
    for idx, i in enumerate(ports):
        route1 = route[:]
        route1.append(i)

        ports1 = ports[:idx] + ports[idx+1:]

        if (len(ports) == 1):
            # Print the port names in route when the recursion terminates
            distance = D[route1[0]][route1[1]] + D[route1[1]][route1[2]] + D[route1[2]][route1[3]] + D[route1[3]][route1[4]]
            emissions = distance * co2
            # print(' '.join([portnames[i] for i in route1]) + " %.1f kg" % emissions)
            if(smallest > emissions) :
                smallest = emissions
                bestroute = route1
        else:
            permutations(route1, ports1)

def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing

    # this will start the recursion 
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()
