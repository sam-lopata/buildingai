countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

# total_male_fishers = sum(male_fishers)
# total_female_fishers = sum(female_fishers)
# total_fishers = total_male_fishers + total_female_fishers
# total_population = sum(populations)
    
def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
        total_fishers = sum(female_fishers)
    else:
        fishers = male_fishers
        total_fishers = sum(male_fishers)

    guess = None
    biggest = 0.0
    
    for i in range(0, len(countries)):
        p = fishers[i]/total_fishers*100
        if p>biggest:
            guess=countries[i]
            biggest=p
        
    return (guess, biggest)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()
