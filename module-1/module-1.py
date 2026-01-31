# Suresh Shrestha
# 1/17/2026
# Module 1.3 Assignment

# This program asks the user for the number of bottles of beer on the wall, counts down to one using a
# function with correct lyrics, and then reminds the user to buy more beer.

def countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print("Take one down and pass it around,"
              f"{bottles - 1} {'bottle' if bottles - 1 == 1 else 'bottles'} of bear on the wall.\n")
        bottles -= 1

    # handle the last bottle
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, 0 bottle(s) of beer on the wall.\n")

def main():
    bottles = int(input("Enter number of bottles: "))
    countdown(bottles) 
    print("Time to buy more bottles of beer.")

main()  