play_again = "Y"

def game():

   import random

   secret_number = random.randint(1, 10)

   print "I'm thinking of a number between 1 and 10."

   count = 5

   while True:
       print "You have %d guesses left." % count
       number_input = int(raw_input("What's the number?"))
       if number_input > secret_number:
           print "%d is too high" % number_input
           count -= 1
       elif number_input < secret_number:
           print "%d is too low" % number_input
           count -= 1
       else:
           print "Yes! You win!"
           global play_again
           play_agian = raw_input("Do you want to play again (Y or N)?")
           break
       if count < 1:
           print "You ran out of guesses"
           global play_again
           play_again = raw_input("Do you want to play again (Y or N)?")
           break

while True:
   if play_again == "Y":
       game()
   elif play_again == "N":
       print "Bye"
       break
