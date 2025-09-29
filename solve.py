class Board:
    def __init__(self):
        self.grid=[[" " for _ in range(3)] for _ in range(3)] 
    
    def display(self):
        print(f" {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]}")
        print('-----------')
        print(f" {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]}")
        print('-----------')
        print(f" {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]}")
    
    def update_cell(self, row, col, player):
            if self.grid[row][col] == " ":
                self.grid[row][col] = player
                return True
            else:
                print("cell already occupied! Try again.")
                return False
    
    def check_win(self, player):
            # rows
            for row in range(3):
                if self.grid[row][0] == player and self.grid[row][1] == player and self.grid[row][2] == player:
                    return True
            # columns
            for col in range(3):
                if self.grid[0][col] == player and self.grid[1][col] == player and self.grid[2][col] == player:
                    return True
            # diagonals
            if self.grid[0][0] == player and self.grid[1][1] == player and self.grid[2][2] == player:
                return True
            if self.grid[0][2] == player and self.grid[1][1] == player and self.grid[2][0] == player:
                return True
            return False
    
    def check_draw(self):
            for row in range(3):
                for col in range(3):
                    if self.grid[row][col] == " ":
                        return False
            return True





       #Main game Loop 
class TikTacToe:
     def __init__(self):
        self.board=Board()
        self.current_player="X"

     def switch_player(self):
        self.current_player="O" if self.current_player=="X" else "X"

     def play(self):
         while True:
             self.board.display()
             print(f"Player {self.current_player}'s turn.")

             #Take input
             row = int(input("Enter row (0, 1, 2):")) 
             col =int(input("Enter col (0, 1, 2):")) 

        #check win
             if self.board.update_cell(row, col , self.current_player):
                 if self.board.check_win(self.current_player):
                       self.board.display()
                       print(f" Congratulations!!! Player {self.current_player} You've won")
                       break
              

                     #check draw
                 if self.board.check_draw():
                        self.board.display()
                        print("Its a draw!")
                        break
                  
                 self.switch_player()

if __name__ == "__main__":
     game=TikTacToe()
     game.play()
         



                  


              
              






               
               




    



             
                        

        








 
 
