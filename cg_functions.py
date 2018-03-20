# camel game with functions

import random
import time

print(time.asctime())

def authenticate():
     total_triesUser=0
     total_triesPass=0
     while total_triesUser<4 and total_triesPass<4:
          theUsername=str(input("Enter your username, the press Return/Enter: "))
          if theUsername=='com':
               total_triesUser+=4
               print("Username successful")
               while total_triesPass<4:
                     thePassword=str(input("Enter the password, then press Return/Enter: "))
                     if thePassword=='127':
                          total_triesPass+=4
                          init()
                     else:
                          print("Unable to log in. ")
                          total_triesPass+=1
                          if total_triesPass>3:
                               break                         
          else:
               print("Username Incorrect.")
               total_triesUser+=1
               if total_triesUser>3:
                    break
               
               
     
    
def init():
     print()
     print("-------------------")
     print("Welcome to the Camel Game")
     print("You have stolen a camel to make your way across the great Mobi desert.")
     print("The natives want their camel back and are chasing you down!")
     print("Survive your desert trek and out run the natives.")
     print("--------------------")
     time.sleep(2)
     main()



def main():
     milesTraveled = 0
     thirst = 0
     camelFatigue = 0
     nativesTraveled = -20
     canteen = 3
     oasis=0
     nativesBehind=0
     done = False
     
     while not done:
         nativesBehind = milesTraveled - nativesTraveled
         fullSpeed = random.randrange(10, 21)
         moderateSpeed = random.randrange(5, 13)
         print("""
         A. Drink from your canteen.
         B. Ahead at moderate speed.
         C. Ahead full speed.
         D. Stop for the night.
         E. Status check
         Q. Quit.""")
         print()
         userInput = input("Select a choice: ")
         if userInput.lower() == "q":
             break
     #status
         elif userInput.lower() == "e":
             print("Miles traveled: ",milesTraveled)
             print("Drinks in canteen: ",canteen)
             print("Your camel has ",camelFatigue,"amount of fatigue.")
             print("The natives are ",nativesBehind,"miles behind you.")
     #stop for night
         elif userInput.lower() == "d":
             #camelFatigue *= 0
             camelFatigue=0
             print("Your camel feels refreshed and happy his fatigue is now ",camelFatigue)
             nativesTraveled += random.randrange(7, 15)
     #move full speed
         elif userInput.lower() == "c":
             print("You traveled ",fullSpeed,"miles!")
             milesTraveled += fullSpeed
             print("Overall, you traveled ",milesTraveled)
             thirst += 1
             camelFatigue += random.randrange(1, 4)
             nativesTraveled += random.randrange(7, 15)
             oasis = random.randrange(1, 21)

     #move moderate speed
         elif userInput.lower() == "b":
             print("You traveled ",moderateSpeed,"miles!")
             milesTraveled += moderateSpeed
             print("So far, you traveled ",milesTraveled,"miles!")
             thirst += 1
             camelFatigue += 1
             nativesTraveled += random.randrange(7, 15)
             oasis = random.randrange(1, 21)

     #drink canteen
         elif userInput.lower() == "a":
             if canteen == 0:
                 print("You're out of water.")
             else:
                 canteen -= 1
                 thirst = 0
                 print("You have ",canteen,"drinks left and you are no longer thirsty.")

     #not done check
         if oasis == 20:
             camelFatigue = thirst = 0
             canteen = 3
             print("You found an oasis! After taking a drink you filled your canteen and the camel is refreshed.")
         if nativesBehind <= 15:
             print("The natives are drawing near!")
         if milesTraveled >= 200: #and not done:
             print("You've traveled: ", milesTraveled, "You made it across the desert.You won!!")
             #done = True
             break
         if nativesTraveled >= milesTraveled:
             print("The natives caught and beheaded you.")
             print("You're dead!")
             userInput=input("Would you like to play the game again? Y/N: ")
             if userInput=="y" or userInput=="Y":
                 init()
             else:
                 break
             #done = True
         if thirst > 4 and thirst <= 6: #and not done:
             print("You are thirsty")
         if thirst > 6:
             print("You died of dehydration!")
             userInput=input("Would you like to play the game again? Y/N: ")
             if userInput=="y" or userInput=="Y":
                 init()
             else:
                 break
         if camelFatigue > 5 and camelFatigue <= 8: #and not done:
             print("Your camel is getting tired.")
         if camelFatigue > 8:
             print("Your camel is dead.")
             print()
             userInput=input("Would you like to play the game again? Y/N: ")
             if userInput=="y" or userInput=="Y":
                 init()
             else:
                 done=True


authenticate()






