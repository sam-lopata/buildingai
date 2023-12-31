import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    count = 0
    # define this function and return the number of occurrences as a number
    p = np.array([1,1,1,1,1])
    for i in range(0, len(seq)-(len(p)-1)):
        tmp = seq[i:(i+len(p))]
        comparison = tmp == p
        if comparison.all():
            count +=1
      
    return count

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
