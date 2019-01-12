import os
import board 

b = board.board()

print("Welcome to the TicTacToe\n")
print("Game Mode\n")
print("1.PVC\n")
print("2.PVP\n")
m = int(input("Please choose a game model:"))


def main():
    os.system("cls")
    b.b()
        

while True:
    if (m == 1):
         main()
       
         x = int(input("Please enter a position for X put in (1-9):"))
         b.update_cell(x, "X")

         if b.win("X"):
            print("\nX wins!\n")
            play_again = input("Would you like to play again?(Y/N):")
            if play_again == "Y":
               b.reset()
               continue   
            else:
              break

         if b.is_tie():
            print("\nTie Game\n")
            play_again = input("Would you like to play again?(Y/N):")
            if play_again == "Y":
               b.reset()
               continue               
            else:
              break

         b.AI_move("O")

         if b.win("O"):
            print("\nO wins!\n")
            play_again = input("Would you like to play again?(Y/N):")
            if play_again == "Y":
               b.reset()
               continue               
            else:
              break

         if b.is_tie():
            print("\nTie Game\n")
            play_again = input("Would you like to play again?(Y/N):")
            if play_again == "Y":
               b.reset()
               continue               
            else:
              break



    elif(m == 2):
         main()
       
         x = int(input("Please enter a position for X put in (1-9):"))
         
         b.update_cell(x, "X")
         main()

         if b.win("X"):
            print("\nX wins!\n")
            play_again = input("Would you like to play again?(Y/N):")
            if play_again == "Y":
              b.reset()
              continue              
            else:
              break
         
         if b.is_tie():
            print("\nTie Game\n")
            play_again = input("Would you like to play again?(Y/N):")
            if play_again == "Y":
               b.reset()
               continue               
            else:
              break

         o= int(input("Please enter a position for O put in (1-9):"))
         b.update_cell(o, "O")

         if b.win("O"):
            print("\nO wins!\n")
            play_again = input("Would you like to play again?(Y/N):")
            if play_again == "Y":
              continue
            else:
              break

         if b.is_tie():
            print("\nTie Game\n")
            play_again = input("Would you like to play again?(Y/N):")
            if play_again == "Y":
               b.reset()
               continue               
            else:
              break