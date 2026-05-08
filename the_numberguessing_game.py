import random
import pyttsx3
computer= random.randint(1,100)
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak("  IN THIS GAME YOU HAVE TO GUESS A NUMBER \n BETWEEN RANGE 1-100 \n \t\t YOU HAVE ONLY 6 GUESSES")
print("  IN THIS GAME YOU HAVE TO GUESS A NUMBER \n BETWEEN RANGE 1-100 \n \t\t YOU HAVE ONLY 6 GUESSES")



user_input = input("GUESS A NUMBER FROM 1 TO 100 :-")
if user_input.isdigit():
    n = int(user_input)
  
else:
    print("Please enter a valid number!")
    speak("Please enter a valid number!")



for i in range (1,6):
    if(computer>n):
        speak("    GO HIGHER! ")
        print("    GO HIGHER! ")
        n=int(input("GUESS THE NUMBER AGAIN :-"))
    if(n==computer):
        print(F"    YOU GUESS PERFECT THAT IS {n}")
        speak(F"    YOU GUESS PERFECT THAT IS {n}")
        with open("gussing_game_result.txt","a") as f: 
            print(f" YOU GUSSED PERFECT IN {i+1} TRIES" ,file=f)
                    
        break
    if(computer<n):
        print("    GO LOWER!")
        speak("    GO LOWER!")
        n=int(input("GUESS THE NUMBER AGAIN :- "))
else:
    print(f"YOU TRIES ARE OVER !\n THE NUMBER IS  {computer}")
    speak(f"YOU TRIES ARE OVER !\n THE NUMBER IS  {computer}")
    with open("gussing_game_result.txt","a") as f :
        print(f"YOU FAILED TO GUESS THE NUMBER {computer}", file=f)



