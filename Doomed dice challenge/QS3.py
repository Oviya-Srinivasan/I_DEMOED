from fractions import Fraction

# Define the dice
die_A = [1, 2, 3, 4, 5, 6]
die_B = [1, 2, 3, 4, 5, 6]

# Calculate the total number of combinations
total_combinations = len(die_A) * len(die_B)

# Initialize a dictionary to store the distribution of sums
sum_distribution = {i: 0 for i in range(2, 13)}

# Calculate the distribution of all possible sums
for a in die_A:
    for b in die_B:
        sum_distribution[a + b] += 1

# Calculate and print the probability of each sum
print("Probability of all possible sums:")
for sum, count in sum_distribution.items():
    probability = Fraction(count, total_combinations)
    print(f"P(Sum = {sum}) = {probability}")
