import random #this brings the tool of rng into this code so this game can be made 

print("🎮 Guess the Number Game") #title of the game gets printed first 
print("Computer picked a number 1-10. Guess it.") #instructions for how to play the game aka request

secret = random.randint(1, 10,) # list of numbers you can pick from
attempts = 0 

while True: 
    try:
        guess = int(input("Your guess: ")) #user inputs a number from 1 to 10 
        attempts += 1 # attemp tracker will be logged soon
        
        if guess < secret: # if you guess 1 and the number is 5 then it print too low because of the fact you went under the value
            print("Too low 📉")
        elif guess > secret: #if you guess 10 when the number is 1 you would have guessed too high and it would print a too high that's about it
            print("Too high 📈")
        else:
            print(f"✅ Correct! You got it in {attempts} tries")
            print("That's how backend works: you send a request, I respond.")
            break
    except ValueError:
        print("Enter a number, genius.")
"# Updated documentation" 
