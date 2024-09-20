#!/usr/bin/env python3
# Author: Parisha Puri
# Author ID: ppuri9
# Date Created: 2024/09/19

import sys

# Assign the first command line argument as the timer value, converted to an integer
timer = int(sys.argv[1])

# While loop to count down from the timer value to 1
while timer > 0:
    print(timer)
    timer -= 1

# Print 'blast off!' after the loop finishes
print('blast off!')

