import random

def guess_the_number():
  """
  Generates a random number and challenges the user to guess it.
  """
  # Generate a random number between 1 and 100 (inclusive)
  secret_number = random.randint(1, 100)
  num_guesses = 0

  while True:
    try:
      # Get user guess
      guess = int(input("Guess a number between 1 and 100: "))
      num_guesses += 1

      # Check guess
      if guess == secret_number:
        print(f"Congratulations! You guessed the number in {num_guesses} attempts.")
        break
      elif guess < secret_number:
        print("Too low, try again!")
      else:
        print("Too high, try again!")
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  guess_the_number()
