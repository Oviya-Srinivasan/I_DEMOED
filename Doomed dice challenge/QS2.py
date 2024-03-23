# Define the dice
die_A = [1, 2, 3, 4, 5, 6]
die_B = [1, 2, 3, 4, 5, 6]

# Print the header
print("(A ,B) ", end="")
for b in die_B:
    print(f"B={b} ", end="")
print()

# Print the distribution of all possible combinations
for a in die_A:
    print(f"A={a}: ", end="")
    for b in die_B:
        print(f"({a},{b}) ", end="")
    print()
