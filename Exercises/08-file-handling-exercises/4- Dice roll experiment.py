# Dice roll experiment
import random
def rolls():
    rolls_10 = [random.randint(1,6) for i in range(10)]
    rolls_100 = [random.randint(1,6) for i in range(100)]
    rolls_1000= [random.randint(1,6) for i in range(1000)]
    rolls_10000 = [random.randint(1,6) for i in range(10000)]
    rolls_100000 = [random.randint(1,6) for i in range(100000)]
    return rolls_10, rolls_100, rolls_1000, rolls_10000, rolls_100000

def frequency():
    results = []
    for roll in rolls():
        counts = [roll.count(i) for i in range(1,7)]
        results.append(counts)
    return results

def probability():
    probabilities = []
    frequencies = frequency()

    for counts in frequencies:
        total_rolls = sum(counts)
        prob_for_set = []
        for c in counts:
            prob = c / total_rolls
            prob_for_set.append(prob)
        
        probabilities.append(prob_for_set)
    return probabilities

def main():
    freqs = frequency()
    probs = probability()
    rolls_list = [10, 100, 1000, 10000, 100000]
    names = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]

    with open("simulation.txt", "w") as f:
        for idx, n in enumerate(rolls_list):
            f.write(f"Number of rolls: {n}\n")
            for j in range(6):
                f.write(f"{names[j]}: {freqs[idx][j]}, probability: {probs[idx][j]:.3f}\n")
            f.write("\n")

# Ngl, used a lot of chatGPT for my main function

main()