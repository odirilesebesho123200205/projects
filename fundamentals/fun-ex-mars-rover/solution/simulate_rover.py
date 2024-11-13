import sys
import math

path_to_instructions = sys.argv[1]
with open(path_to_instructions, "r") as file:
    instructions = [line.strip() for line in file]

# The rover starts at the origin facing north.
x, y = 0, 0
facing = 0

for instruction in instructions:
    print(instruction)
    print(x, y, facing)