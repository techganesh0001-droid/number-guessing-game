count = 0
attempts = 7
secretcode = 9

user = input("Enter your username: ")

while attempts > 0:
    usercode = int(input("Enter your secret code: "))

    count += 1
    attempts -= 1

    if usercode == secretcode:
        print("Welcome", user)
        print("You guessed it in", count, "attempt(s)")
        break

    elif usercode > secretcode:
        print("Your code is greater than the secret code")

    else:
        print("Your code is less than the secret code")

    print(attempts, "attempts left")

else:
    print("You have exhausted all attempts.")
    print("Game Over!")
    print("The secret code was:", secretcode)
