import random
from IPython.display import clear_output


board_choices = {"a1": "/", "b1": "/","c1" : "/","a2": "/", "b2": "/","c2": "/","a3": "/", "b3": "/", "c3": "/"}

board_keys = []

for key in board_choices:
    board_keys.append(key)

player1_c = []
bot_options = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
bot_c = []
all_draw = []
    
def board_create(board):
    print("  a b c")
    print("1 " + board["a1"] + "|" + board["b1"] + "|" + board["c1"])
    print("  ------")
    print("2 " + board["a2"] + "|" + board["b2"] + "|" + board["c2"])
    print("  ------")
    print("3 " + board["a3"] + "|" + board["b3"] + "|" + board["c3"])

def check(choice: str, marker: str):
    player_choice = choice

    if player_choice == "a1":
        board_choices["a1"] = marker

    elif player_choice == "a2":
        board_choices["a2"] = marker

    elif player_choice == "a3":
        board_choices["a3"] = marker

    elif player_choice == "b1":
        board_choices["b1"] = marker

    elif player_choice == "b2":
        board_choices["b2"] = marker

    elif player_choice == "b3":
        board_choices["b3"] = marker

    elif player_choice == "c1":
        board_choices["c1"] = marker

    elif player_choice == "c2":
        board_choices["c2"] = marker

    elif player_choice == "c3":
        board_choices["c3"] = marker

    
print("start game? Y/N")

player1 = input()


if player1 == "Y":
    board_create(board_choices) # AVSLUTAR PROGGRAMET
else:
    # HÄR
    pass
        
i = 0
while outer := True:
    if i % 2 == 0:
        inner = True
        print("player turn")
        while inner == True:
            player_choice = input()
            
            if player_choice in all_draw:
                continue
            else:
                all_draw.append(player_choice)
                check(player_choice, "X")
                inner = False
    else:
        inner = True
        print("Bots turn")
        while inner == True:
            player_choice = random.choice(bot_options)

            if player_choice in all_draw:
                continue
            else:
                all_draw.append(player_choice)
                check(player_choice, "O")
                inner = False
    i += 1
    # clear_output(wait=True) BUGGED

    board_create(board_choices)
        

        
    




    
    

    


    




