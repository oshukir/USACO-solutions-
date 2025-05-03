import sys
import random
 
n, target = map(int, input().split())
values = list(map(int, input().split()))
 
# Generate a random large constant for XOR transformations
RANDOM = random.randrange(2**62)
 
def wrap(x):
    """ Apply a random XOR transformation to prevent hash collisions """
    return x ^ RANDOM
 
val_to_ind = {}
 
for i, val in enumerate(values, start=1):
    if wrap(target - val) in val_to_ind:
        print(i, val_to_ind[wrap(target - val)])
        sys.exit(0)
    val_to_ind[wrap(val)] = i  # Store the wrapped key
 
print("IMPOSSIBLE")
