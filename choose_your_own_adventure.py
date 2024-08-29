
name = input("type your name: ")
print ("welcome", name ,"to this adventure!")
answer = input("you are on dirt road, it come to an end and you can go left and right. Which way you would like to go? ").lower()
if answer =="left":
     answer = input("you can come to river,you can walk around it or swim accross? Type walk to walk around and swim to swim accross:")

     if answer == "swim":
          print(" You swam across and were eaten by alligator.")
     elif answer == "walk":
          print("you walked for a mile , Ran out of water  and you lost the game.")
     else:
          print('not a valid option .You lose.')

elif answer == "right":
     answer = input("you come to a bridge, it look wobbly, Do you want to cross it. or Head back(cross/back)?")

     if answer == "back":
          print("you go back and lose ok boy or girl who ever is playing.")

     elif answer == "cross":
         answer = input("you cross the bridge and you meet a stranger. You talk to them (yes/no)?")
         if answer == "yes":
              print("you talk to the stranger and they give you gold. YOU WIM!")
    
         elif answer == "no":
              print("you ignore the stranger they are offended and they kill you which means you. LOSEEEEE! ")

     else:
          print('not a valid option .You lose.')
else: 
     print('not a valid option. you lose.')
print("thankyou for trying, name ")