# example of int
chocolate: int = 1

# example of float
cheese: float = 3.1

# example of str
character: str = "Liz Lemon"

# example of bool
has_food: bool = True

# print variables
print(chocolate)
print(cheese)
print(character)
print(has_food)

# concatenate
print(character + " has " + str(chocolate) + " chocolate bar and " + str(cheese) + " pounds of cheese.")

# if-else statement
if has_food is True:
  print("I have food!")
else:
  print("I need more food.")