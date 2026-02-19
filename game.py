import random

print("🎮 Guess the Number Game")
print("Computer picked a number 1-10. Guess it.")

secret = random.randint(1, 10,)
attempts = 0

while True:
    try:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess < secret:
            print("Too low 📉")
        elif guess > secret:
            print("Too high 📈")
        else:
            print(f"✅ Correct! You got it in {attempts} tries")
            print("That's how backend works: you send a request, I respond.")
            break
    except ValueError:
        print("Enter a number, genius.")
