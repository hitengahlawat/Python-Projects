
import random
import pyttsx3

computer = random.randint(1, 100)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

message = """
IN THIS GAME YOU HAVE TO GUESS A NUMBER
BETWEEN RANGE 1-100
YOU HAVE ONLY 5 GUESSES
"""

print(message)
speak(message)

for i in range(1, 6):

    n = int(input(f"Attempt {i}: GUESS A NUMBER FROM 1 TO 100 :- "))

    if n == computer:
        print(f"YOU GUESSED PERFECTLY! THAT IS {n}")
        speak(f"YOU GUESSED PERFECTLY! THAT IS {n}")

        with open("gussing_game_result.txt", "a") as f:
            print(f"YOU GUESSED PERFECTLY IN {i} TRIES", file=f)

        break

    elif n < computer:
        print("GO HIGHER!")
        speak("GO HIGHER!")

    else:
        print("GO LOWER!")
        speak("GO LOWER!")

else:
    print(f"YOUR TRIES ARE OVER!\nTHE NUMBER WAS {computer}")
    speak(f"YOUR TRIES ARE OVER! THE NUMBER WAS {computer}")

    with open("gussing_game_result.txt", "a") as f:
        print(f"YOU FAILED TO GUESS THE NUMBER {computer}", file=f)