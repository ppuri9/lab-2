#!/usr/bin/env python3

import sys

# Check if the number of arguments is exactly 3 (including the script name)
if len(sys.argv) == 1:
    # No arguments provided
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

elif len(sys.argv) != 3:
    # Incorrect number of arguments provided
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# Assign command line arguments to 'name' and 'age'
name = sys.argv[1]
age = sys.argv[2]

# Print the final message
print(f"Hi {name}, you are {age} years old.")

