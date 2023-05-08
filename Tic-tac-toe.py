
import random

board_choices = {"a1": "/", "b1": "/","c1" : "/","a2": "/", "b2": "/","c2": "/","a3": "/", "b3": "/", "c3": "/"}

board_keys = []

for key in board_choices:
    board_keys.append(key)
turns = 0
player1_c = []
bot_options = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
bot_c = []
    
def board_create(board):
    print("  a b c")
    print("1 " + board["a1"] + "|" + board["b1"] + "|" + board["c1"])
    print("  ------")
    print("2 " + board["a2"] + "|" + board["b2"] + "|" + board["c2"])
    print("  ------")
    print("3 " + board["a3"] + "|" + board["b3"] + "|" + board["c3"])
    
    
player1 = input()

print("start game? Y/N")

if player1 == "Y":
    for i in range(1):
        board_create(board_choices)
        
print("player turn 1"):
    turns += 1
        
player_choice = input()

if player_choice == "a1":
        board_choices["a1"] = "X"

elif player_choice == "a2":
    board_choices["a2"] = "x"
    
elif player_choice == "a3":
    board_choices["a3"] = "x"
    
elif player_choice == "b1":
    board_choices["b1"] = "x"
    
elif player_choice == "b2":
    board_choices["b2"] = "x"
    
elif player_choice == "b3":
    board_choices["b3"] = "x"
    
elif player_choice == "c1":
    board_choices["c1"] = "x"
    
elif player_choice == "c2":
    board_choices["c2"] = "x"
    
elif player_choice == "c3":
    board_choices["c3"] = "x"
    
for i in range(1):
    board_create(board_choices)
    
print("computer turn 1"):
    turns +=1
    
random_choice = random.choice(bot_options)
print(random_choice)

if random_choice == "a1":
    board_choices["a1"] = "o"
    
elif random_choice == "a2":
    board_choices["a2"] = "o"
    
elif random_choice == "a3":
    board_choices["a3"] = "o"

elif random_choice == "b1":
    board_choices["b1"] = "o"
    
elif random_choice == "b2":
    board_choices["b2"] = "o"
    
elif random_choice == "b3":
    board_choices["b3"] = "o"
    
elif random_choice == "c1":
    board_choices["c1"] = "o"
    
elif random_choice == "c2":
    board_choices["c2"] = "o"
    
elif random_choice == "c3":
    board_choices["c3"] = "o"

for i in range(1):
    board_create(board_choices)
    
print("player turn 2"):
    turns += 1

player_choice = input()

for i in range(1):
    board_create(board_choices)
    




    
    

    


    




