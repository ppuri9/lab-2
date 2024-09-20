#!/usr/bin/env python3
# Author: Parisha Puri
# Author ID: ppuri9
# Date Created: 2024/09/19

import sys

# Check if a command line argument is provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Use the argument as the timer value
else:
    timer = 3  # Default timer value

# While loop to count down from the timer value to 1
while timer > 0:
    print(timer)
    timer -= 1

# Print 'blast off!' after the loop finishes
print('blast off!')

