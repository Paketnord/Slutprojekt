board_choices = {"a1": "/", "b1": "/","c1" : "/","a2": "/", "b2": "/","c2": "/","a3": "/", "b3": "/", "c3": "/"}

board_keys = []

for key in board_choices:
    board_keys.append(key)
player1_c = []
bot_c = []
turns = []
    
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
else:
    
    

    


    




