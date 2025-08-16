import os

for root, dirs, files in os.walk("."):
    print("Directory:", root)
    print("Subdirectories:", dirs)
    print("Files:", files)
    print("-" * 30)