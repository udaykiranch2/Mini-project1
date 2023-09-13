import random
actions = ["rock","paper","scissors"]
for x in actions:
    print(f"{actions.index(x)+1}.{x}")

def get_user_selection(actions,question):
    n = len(actions)
    
    for i in range(n):
        try:
            i = int(input(question)) - 1
            action = actions[i]
            return action
        except IndexError:
            print("valid number")
            
            
def get_device_selection():
    selection = random.randint(0,len(actions)-1)
    action1=actions[selection]
    return action1
 
def get_winner(action,action1):
    
    if action == action1:
        print("tied,try again")
    elif action == 'rock':
        if action1 == 'paper':
            print("paper covers rock,You lost")
        else:
            print("rock breaks scissor,You won!")
    elif action == 'paper':
        if action1 == 'rock':
            print("paper covers rock,You won!")
        else:
            print("scissor cut paper,You lost")
    elif action == 'scissors':
        if action1 == 'paper':
            print("scissor cut paper,You won!")
        else:
            print("rock breaks scissor,you lost")
    return ""
            
while True:           
    user_action=get_user_selection(actions,"select one choice:")
    device_action = get_device_selection()
    print(get_winner(user_action,device_action))
    res = input("would you like to continue?(y/n)")
    if res == 'n':
        break

    
    
