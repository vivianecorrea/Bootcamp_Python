# import turtle
#
# maya = turtle.Turtle()
# maya.shape("turtle")
# maya.color("cyan")
# maya.forward(100)
# my_screen= turtle.Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
table.align = "l"

print(table)
