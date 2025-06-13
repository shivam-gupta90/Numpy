#Simulate 100 dice rolls and count the frequency of each outcome.

import numpy as np

# Simulate 100 dice rolls (values from 1 to 6)
rolls = np.random.randint(1, 7, size=100)

# Count the frequency of each outcome from 1 to 6
counts = np.bincount(rolls)[1:]  # Skip index 0 (not used)

# Display results
for i, count in enumerate(counts):
    print(f"Dice face {i}: {count} times")
