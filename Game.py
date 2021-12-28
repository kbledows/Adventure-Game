from Player import Character
from Item import Item
import time

def main():
    print("Hello World!")
    print("Please enter a name")
    name = input()
    print("Please enter a sex")
    sex = input()

    p = Character(name,sex)
    print(p.name)
    print(p.sex)

if __name__ == "__main__":
	main()