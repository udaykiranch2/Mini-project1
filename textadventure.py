def menu(list,question):
    n = len(list)
    for i in range(n) :
        try:
            i = int(input(question)) - 1
            entry = list[i]
            return entry
        except IndexError:
             print("give a proper input")

        
items = ["pot plant","painting","vase","lamp-shade","shoe","door"]
keyword = 'vase'
keyfound=0
loop = 1
print("you found yourself locked in room")
print(f'{len(items)} things available in room are')
for x in items:
    print (x)
print("")
print("could there be a key some where in the room")
while loop ==1:
    choice = menu(items,"what do you want to inspect?")
    if keyfound == 0:
        if choice == keyword:
                print(f"you found key in {keyword}")
                print("")
                break
        else:
                print(f"you found nothing in {choice}")
    
 
   

        





