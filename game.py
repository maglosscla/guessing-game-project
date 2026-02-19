import random  # brings the tool of rng into this code

print("🎮 Guess the Number Game - WITH DIFFICULTY!")
print("=" * 40)

# DIFFICULTY SELECTION - NEW FEATURE!
print("Choose difficulty:")
print("1️⃣ Easy   (1-10, unlimited attempts)")
print("2️⃣ Medium (1-50, 10 attempts)")
print("3️⃣ Hard   (1-100, 5 attempts)")
print("4️⃣ Impossible (1-1000, 3 attempts)")

while True:
    try:
        choice = int(input("Enter difficulty (1-4): "))
        if choice in [1, 2, 3, 4]:
            break
        else:
            print("Please enter 1, 2, 3, or 4")
    except ValueError:
        print("Enter a number, genius.")

# SET DIFFICULTY PARAMETERS
if choice == 1:  # Easy
    max_number = 10
    max_attempts = float('inf')  # Unlimited
    difficulty_name = "Easy"
elif choice == 2:  # Medium
    max_number = 50
    max_attempts = 10
    difficulty_name = "Medium"
elif choice == 3:  # Hard
    max_number = 100
    max_attempts = 5
    difficulty_name = "Hard"
else:  # Impossible
    max_number = 1000
    max_attempts = 3
    difficulty_name = "Impossible"

# GENERATE SECRET NUMBER based on difficulty
secret = random.randint(1, max_number)
attempts = 0

print(f"\n🎯 {difficulty_name} mode: Guess 1-{max_number}")
if max_attempts != float('inf'):
    print(f"⚠️  You have {max_attempts} attempts!")

# MAIN GAME LOOP
while True:
    # Check if attempts exceeded (for limited modes)
    if max_attempts != float('inf') and attempts >= max_attempts:
        print(f"\n💀 GAME OVER! No attempts left.")
        print(f"The number was: {secret}")
        break
        
    try:
        guess = int(input("\nYour guess: "))
        attempts += 1
        
        # Check if guess is in range
        if guess < 1 or guess > max_number:
            print(f"❌ Guess must be between 1 and {max_number}")
            continue
            
        if guess < secret:
            print("📉 Too low!")
            if max_attempts != float('inf'):
                print(f"Attempts left: {max_attempts - attempts}")
        elif guess > secret:
            print("📈 Too high!")
            if max_attempts != float('inf'):
                print(f"Attempts left: {max_attempts - attempts}")
        else:
            print(f"\n🎉✅ CORRECT! You got it in {attempts} tries!")
            
            # RATING BASED ON PERFORMANCE
            if attempts == 1:
                print("🔥 MIND READER! Are you cheating?")
            elif attempts <= 3:
                print("⭐ Excellent guessing!")
            elif attempts <= 7:
                print("👍 Good job!")
            else:
                print("😅 You got there eventually!")
                
            print("That's how backend works: you send a request, I respond.")
            break
            
    except ValueError:
        print("❌ Enter a NUMBER, genius. Not letters.")