# <destroyerasdfdev@gmail.com> || Nicholaus Whites
# <9/21/2018>
# <My first full text game for fun>

prompt = '> '
ask = ""
inv = ""
floor = ""
global takenDirt
takenDirt = 0
takedyrn = 0
pHealth = 100

#=========================================Define=========================================================#




def shackAscii():
        print("You are in front of a shack.\nYou see a Field to the West")
        print("         /     ___      \            ")
        print("          |   |_|_|   x|             ")
        print("          |   |_|_|    |             ")
        print("          | x        # |             ")
        print("          |    ____    |             ")
        print("          |    |  |  x |             ")
        print("          |  # |* |    |             ")
        print("__________|____|__|____|_____________")
        
def insideShackAscii():
        print("The inside of the shack looks completly different than what you would expect from the outside")
        print("""       |                                          |         """)
        print("""       |                                          |         """)
        print("""       |                                          |         """)
        print("""       |                                          |         """)
        print("""       |__________________________________________|         """)
        print("""       /                                          \         """)
        print("""      /                 ___________                \        """)
        print("""     /                 |           |                \       """)
        print("""    /                  | 0=|====>  |                 \      """)
        print("""   /                   |___________|                  \     """)
        print("""  /                                                    \    """)
        print(""" /                                                      \   """)
        print("""/                                                        \  """)
        print("There is a sword on the pedistal in the middle of the room.     ")
        dyrnwynLook()

def dyrnwynLook():
        print("""
      /| ________________
0|===|* >________________>
      \|
It is inscribed with 'Dyrnwyn'              """)

def insideShackAsciiNoD():
        print("The inside of the shack looks completly different than what you would expect from the outside")
        print("""       |                                          |         """)
        print("""       |                                          |         """)
        print("""       |                                          |         """)
        print("""       |                                          |         """)
        print("""       |__________________________________________|         """)
        print("""       /                                          \         """)
        print("""      /                 ___________                \        """)
        print("""     /                 |           |                \       """)
        print("""    /                  |           |                 \      """)
        print("""   /                   |___________|                  \     """)
        print("""  /                                                    \    """)
        print(""" /                                                      \   """)
        print("""/                                                        \  """)
        print("There is a pedistal in the middle of the room.     ")
            #+===========================Take============================================================/\
def takeDirt(inv,takenDirt):
    
    inv = inv + "Dirt       testing        0\n"
    takenDirt = takenDirt + 1
    print("Dirt taken",takenDirt)
    if takenDirt == 5:
        print("What do you need so much dirt for?")
    if takenDirt == 10:
        print("If you keep this up your going to take the whole field...")
    if takenDirt == 20:
        inv = inv + "Field       10\n"
        print("The whole field is now in your pocket... WHAT HAVE YOU DONE!?!?")
        inv = inv.replace("Dirt       testing        0\n","")
    return inv



def inventory(inv):
    if len(inv)==0:
        print("You have nothing in your inventory.")
    else:
        print("Inventory     Type      Val")
        print(inv)
def floors(floor):
    if len(floor)==0:
        print("There is nothing on the floor")
    else:
        print("Everything on the floor:")
        print(floor)


allitems = """Name     Value        Type                            Inventory

              Dirt         0     testing       'Dirt       testing        0\n'
              Dyrnwyn  10000       Sword       'Dyrnwyn      Sword    10000\n'
              """









#=========================================Start=========================================================#
def startingPoint(ask,floor,takenDirt,prompt,inv):
    print("You are in a field.\nYou see a small shack to the East")
    print("""_/\__/_____/_____/_______/__/-___/___""")
    while True:
        ask = input(prompt)
        
        if ask == "look" or ask == "l" or ask == "gl":
            print("You are in a field.\nYou see a small shack to the East")
            print("""_/\__/_____/_____/_______/__/-___/___""")
            floors(floor)
            
        ##taking items start
        elif "take" in ask:
            ##taking dirt from floor
            if "dirt" in ask or "ground" in ask:
                #takeDirt(inv,takenDirt)
                inv = takeDirt(inv,takenDirt)
                print("You put some dirt into your pocket.")
                if "Dirt\n" in floor:
                    floor = floor.replace("Dirt\n","",1)
            ##taking dyrnwyn from floor if there
            elif "dyrnwyn" in ask:
                if "Dyrnwyn\n" in floor:
                    floor = floor.replace("Dyrnwyn\n","",1)
                    inv = inv + 'Dyrnwyn      Sword    10000\n'
                    print("Picked up Dyrnwyn. Flames blaze to life along the blade.")
                else:
                    print("That is not here.")
            else:
                print("That is not here.")
        ##taking items end
        
        elif ask in ["inventory","inv","i"]:
            inventory(inv)
            
        #temp Dropping        
        elif "drop" in ask:
            ##dropping dirt to floor
            if "dirt" in ask:
                if "Dirt       testing        0\n" in inv:
                    if "all" in ask:
                        inv = inv.replace("Dirt       testing        0\n","")
                        print("Dropped all dirt")
                        print("The dirt disappeared into the wind..")
                    else:
                        inv = inv.replace("Dirt       testing        0\n","",1)
                        takenDirt = takenDirt - takenDirt
                        print("You drop some dirt")
                        floor = floor + "Dirt\n"
            ##dropping dyrnwyn to floor
            elif "dyrnwyn" in ask:
                if "Dyrnwyn      Sword    10000\n" in inv:
                    inv = inv.replace("Dyrnwyn      Sword    10000\n","",1)
                    print("You dropped Dyrnwyn. The flames on the blade flicker out.")
                    floor = floor + "Dyrnwyn\n"
                else:
                    print("Testing")
            ##adding new items: make sure to add it to both drop and take for all areas.
            #elif "item" in ask:
            #   if "item   type  val\n" in inv:
            #       inv = inv.replace("item   type  val\n","",1)
            #       print("you dropped item.")
            #       floor = floor + "item\n"
            else:
                print("You do not know how to drop that.")
        #end of item dropping        
        elif "north" in ask:
            print("The only path is east.")
        elif "east" in ask:
            print("You go East.")
            floor = ""
            return inv
            #break
        elif "south" in ask:
            print("The only path is east.")
        elif "west" in ask:
            print("The only path is east.")
        else:
            print("I have no clue what that means...")
            
#startingPoint(ask,floor,takenDirt,prompt,inv)



#================================================East===================================================#
def firstShack(ask,floor,takenDirt,prompt,inv):
    shackAscii()
    while True:
        ask = input(prompt)
        

        
        if ask == "look" or ask == "l" or ask == "gl":
            floors(floor)
            shackAscii()
        ##item taking start
        elif "take" in ask:
            ##takeing dirt from floor if there
            if "dirt" in ask or "ground" in ask:
                if "Dirt" in floor:
                    inv = inv + "Dirt       testing        0\n"
                    floor = floor.replace("Dirt\n","",1)
                    takenDirt += 1
                    print("You put some dirt into your pocket.")
            ##takeing dyrnwyn from floor if there
            elif "dyrnwyn" in ask:
                if "Dyrnwyn\n" in floor:
                    floor = floor.replace("Dyrnwyn\n","",1)
                    inv = inv + 'Dyrnwyn      Sword    10000\n'
                    print("Picked up Dyrnwyn. Flames blaze to life along the blade.")
                else:
                    print("That is not here.")
            ##adding new items: make sure to add it to both drop and take for all areas.
            else:
                print("That is not here.")
                
        ##item taking end

        
        elif ask in ["inventory","inv","i"]:
            inventory(inv)

        #temp Dropping        
        elif "drop" in ask:
            ##dropping dirt to floor
            if "dirt" in ask:
                if "Dirt       testing        0\n" in inv:
                    if "all" in ask:
                        inv = inv.replace("Dirt       testing        0\n","")
                        print("Dropped all dirt")
                        print("The dirt disappeared into the wind..")
                    else:
                        inv = inv.replace("Dirt       testing        0\n","",1)
                        takenDirt = takenDirt - takenDirt
                        print("You drop some dirt")
                        floor = floor + "Dirt\n"
            ##dropping dyrnwyn to floor
            elif "dyrnwyn" in ask:
                if "Dyrnwyn      Sword    10000\n" in inv:
                    inv = inv.replace("Dyrnwyn      Sword    10000\n","",1)
                    print("You dropped Dyrnwyn. The flames on the blade flicker out.")
                    floor = floor + "Dyrnwyn\n"

            ##adding new items: make sure to add it to both drop and take for all areas.
            #elif "item" in ask:
            #   if "item   type  val\n" in inv:
            #       inv = inv.replace("item   type  val\n","",1)
            #       print("you dropped item.")
            #       floor = floor + "item\n"
            else:
                print("You do not know how to drop that.")

                ##        elif "drop" in ask:
##            if "dirt" in ask:
##                if "Dirt         0\n" in inv:
##                    inv = inv.replace("Dirt         0\n","",1)
##                    takenDirt = takenDirt - 1
##                    print("You drop some dirt")
##                    floor = floor + "Dirt\n"
##                else:
##                    print("You do not have that item.")
                
        #end of item dropping


                    
        elif "north" in ask:
            print("You go North.")
            floor = ""
            inv = insideShack(ask,floor,takenDirt,prompt,takedyrn,inv)
            return inv
        elif "east" in ask:
            print("You go East.")
            break
        elif "south" in ask:
            print("You go South")
            break
        elif "west" in ask:
            print("You go West.")
            floor = ""
            inv= startingPoint(ask,floor,takenDirt,prompt,inv)
        else:
            print("I have no clue what that means...")
            

#===========================inside shack=========================================

def insideShack(ask,floor,takenDirt,prompt,takedyrn,inv):
    print("You enter the shack.")
    if "Dyrnwyn      Sword    10000\n" in inv:
        takedyrn = 1
    if takedyrn >= 1:
        insideShackAsciiNoD()
    else:
        insideShackAscii()
    floor = floor + "Dyrnwyn\n"
    while True:
        if "Dyrnwyn      Sword    10000\n" in inv:
            takedyrn = 1
        ask = input(prompt)

        
        
        if ask == "look" or ask == "l" or ask == "gl":
            
            floors(floor)
            if takedyrn >= 1:
                insideShackAsciiNoD()
            else:
                insideShackAscii()
        ##item taking start
        elif "take" in ask:
            ##takeing dirt from floor if there
            if "dirt" in ask or "ground" in ask:
                if "Dirt" in floor:
                    inv = inv + "Dirt       testing        0\n"
                    floor = floor.replace("Dirt\n","",1)
                    takenDirt += 1
                    print("You put some dirt into your pocket.")
            ##takeing dyrnwyn from floor if there
            elif "dyrnwyn" in ask:
                if "Dyrnwyn\n" in floor:
                    if takedyrn >= 1:
                        print("That is not here.")
                    else:
                        takedyrn += 1
                        floor = floor.replace("Dyrnwyn\n","",1)
                        inv = inv + 'Dyrnwyn      Sword    10000\n'
                        print("Picked up Dyrnwyn. Flames blaze to life along the blade.")
            ##adding new items: make sure to add it to both drop and take for all areas.
            else:
                print("That is not here.")
                
        ##item taking end

        
        elif ask in ["inventory","inv","i"]:
            inventory(inv)

        #temp Dropping        
        elif "drop" in ask:
            ##dropping dirt to floor
            if "dirt" in ask:
                if "Dirt       testing        0\n" in inv:
                    inv = inv.replace("Dirt       testing        0\n","",1)
                    takenDirt = takenDirt - takenDirt
                    print("You drop some dirt")
                    floor = floor + "Dirt\n"
            ##dropping dyrnwyn to floor
            elif "dyrnwyn" in ask:
                if "Dyrnwyn      Sword    10000\n" in inv:
                    takedyrn -= 1
                    inv = inv.replace("Dyrnwyn      Sword    10000\n","",1)
                    print("You dropped Dyrnwyn. The flames on the blade flicker out.")
                    floor = floor + "Dyrnwyn\n"
                else:
                    print("Testing")
            ##adding new items: make sure to add it to both drop and take for all areas.
            #elif "item" in ask:
            #   if "item   type  val\n" in inv:
            #       inv = inv.replace("item   type  val\n","",1)
            #       print("you dropped item.")
            #       floor = floor + "item\n"
            else:
                print("You do not know how to drop that.")

                ##        elif "drop" in ask:
##            if "dirt" in ask:
##                if "Dirt         0\n" in inv:
##                    inv = inv.replace("Dirt         0\n","",1)
##                    takenDirt = takenDirt - 1
##                    print("You drop some dirt")
##                    floor = floor + "Dirt\n"
##                else:
##                    print("You do not have that item.")
                
        #end of item dropping


                    
        elif "north" in ask:
            print("There is a wall.")
        elif "east" in ask:
            print("There is a wall.")
        elif "south" in ask:
            print("You leave the house")
            inv = firstShack(ask,floor,takenDirt,prompt,inv)
            break
        elif "west" in ask:
            print("There is a wall.")
        else:
            print("I have no clue what that means...")




#====================game========================            
#start
inv = startingPoint(ask,floor,takenDirt,prompt,inv)

#shack        
inv = firstShack(ask,floor,takenDirt,prompt,inv)

#inside shack
insideShack(ask,floor,takenDirt,prompt,takedyrn,inv)
