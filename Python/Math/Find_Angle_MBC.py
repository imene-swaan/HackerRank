# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import (atan, degrees)

ab = int(input())
bc = int(input())

theta = degrees(atan(ab/bc))
print(f"{round(theta)}"u"\xb0")
