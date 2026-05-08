import random 
s=["stone","paper", "sisor"]
computer=random.choice(s)
my_value=input("enter what you want to choose:-  " )



if my_value=="stone" and computer=="paper":
    print(f" you choose {my_value}")
    print(f"computer choose {computer}")
    print(" YOU LOOSE, TRY NEXT TIME! ")

elif my_value=="paper" and computer=="stone":
    print(f" you choose {my_value}")
    print(f"computer choose {computer}")
    print("CONGRUATS, YOU WIN! ")

if my_value=="paper" and computer=="sisor":
    print(f" you choose {my_value}")
    print(f"computer choose {computer}")
    print(" YOU LOOSE, TRY NEXT TIME! ")

elif(my_value=="sisor" and computer=="paper"):
    print(f" you choose {my_value}")
    print(f"computer choose {computer}")
    print("CONGRUATS, YOU WIN!  ")

if my_value=="sisor" and computer=="stone":
    print(f" you choose {my_value}")
    print(f"computer choose {computer}")
    print(" YOU LOOSE, TRY NXST TIME! ")


elif my_value=="stone" and computer=="sisor":
    print(f" you choose {my_value}")
    print(f"computer choose {computer}")
    print("CONGRUATS, YOU WIN! ")


 
if my_value==computer:
    print(f"computer choose {computer}")
    print(f" you choose {my_value}")
    print(f"ITS DRAW , PLAY NEXT TIME")
    
    
    print("\t\t\t THANKS FOR PLAYING ")
