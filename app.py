#!/usr/bin/env python3

import datetime
import platform
import os

def main():
    """
    A simple Python script that prints system information and current time
    """
    print("=" * 50)
    print("Simple Python Application")
    print("=" * 50)
    
    # Get and display current time
    current_time = datetime.datetime.now()
    print(f"Current time: {current_time}")
    
    # Display system information
    print(f"Python version: {platform.python_version()}")
    print(f"Platform: {platform.platform()}")
    
    # Get and display environment variables
    print("\nEnvironment Variables:")
    for i, (key, value) in enumerate(sorted(os.environ.items())):
        if i < 5:  # Limit to first 5 to keep output clean
            print(f"  {key}: {value}")
    print("  ...")  # Indicate there may be more
    
    # Simulate some work
    print("\nPerforming calculations...")
    result = sum(i * i for i in range(1, 1000000))
    print(f"Sum of squares from 1 to 999999: {result}")
    
    print("\nApplication completed successfully!")

if __name__ == "__main__":
    main()