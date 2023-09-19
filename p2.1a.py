portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
# portnames = ["PAN", "AMS", "CAS", "NYC"]
# print(portnames[1:])
 
def permutations(route, ports, deep=1):
    if (deep == 5):
        return

    # print('deep', deep)
    # print('iroute', route)
    # print('iports', ports)

    # Write your recursive code here
    for idx, i in enumerate(ports):
        # print('deep:idx:i', deep, idx, i)

        route1 = route[:]
        route1.append(i)
        # print('route1', route1)        

        ports1 = ports[:idx] + ports[idx+1:]
        # print('ports1', ports1)
        # print()

        if (len(ports) == 1):
            # Print the port names in route when the recursion terminates
            print(' '.join([portnames[i] for i in route1]))
        else:
            permutations(route1, ports1, deep+1)

# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))
