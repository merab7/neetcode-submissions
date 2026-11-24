class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for  row in board:
                filtered_row = [i for i in row if i != "."]
                if len(filtered_row) != len(set(filtered_row)):
                    return False
    


        cols = [[x[i] for x in board]for i in range(len(board))]
        for  col in cols:
                filtered_col = [i for i in col if i != "."]
                if len(filtered_col) != len(set(filtered_col)):
                    return False
        
        grids = []
        grid_1, grid_2, grid_3 = [],[],[]
        grid_length = 0
        for i in board:

            grid_1+=i[:3]
            grid_2+=i[3:6]
            grid_3+=i[6:]
            grid_length += 3
            if grid_length == 9:
                grids.append(grid_1)
                grids.append(grid_2)
                grids.append(grid_3)
                grid_1,grid_2,grid_3 = [], [], []
                grid_length = 0

        for g in grids:
              filtered_grid = [i for i in g if i != "."]
              if len(filtered_grid) != len(set(filtered_grid)):
                    return False


        
        return True
            



        