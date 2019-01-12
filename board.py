class board():
    def __init__(self):
        self.cells = ["", "", "", "","","","","","",""]
    def b(self):
        print("%s | %s | %s" %(self.cells[1], self.cells[2], self.cells[3]))
        print("--------")
        print("%s | %s | %s" %(self.cells[4], self.cells[5], self.cells[6]))
        print("--------")
        print("%s | %s | %s" %(self.cells[7], self.cells[8], self.cells[9]))
    
    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == "":
            self.cells[cell_no] = player

    def win(self, player):

       for combo in [[1,2,3], [4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
           result = True
           for cell_no in combo:
               if self.cells[cell_no]!=player:
                   result = False

           if result == True:
               return True

       return False
    
    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != "":
                used_cells += 1
        if used_cells == 9:
                return True
        else:
                return False

    def reset(self):
       self.cells = ["", "", "", "","","","","","",""]

    def AI_move(self, player):
        
        for i in range(1, 10):
            if self.cells[5] == "":
               self.update_cell(5, player)
               break

            elif self.cells[i]=="" and self.cells[5] != "":
               
               self.update_cell(i, player)
               break
            
           