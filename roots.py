import numpy as np
import sys

n = input("Provide positive integer to check to: ")
n = float(n)

if n <= 0 or n % 1 != 0:
    print("Sorry, wrong number")
    sys.exit()

for i in range(1, int(n) + 1):
    if np.cbrt(i) % 1 == 0 and np.sqrt(i) % 1 == 0:
        print(i)
print("Check done")