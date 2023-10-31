def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    res = []
    for i in range(0, len(countries)):
        p = (fishers[i]/total_fishers)*100
        res.append(p)
    
    for country, res in zip(countries, res):
        print("%s %.2f%%" % (country, res)) # modify this to print correct results

main()