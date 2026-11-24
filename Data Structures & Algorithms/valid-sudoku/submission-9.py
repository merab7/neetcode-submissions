class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = [[row[i] for row in board] for i in range(len(board))]

        grids = []
        grid_1, grid_2, grid_3 = [], [], []
        grid_length = 0
        for row in board:
            grid_1 += row[:3]
            grid_2 += row[3:6]
            grid_3 += row[6:]
            grid_length += 3
            if grid_length == 9:
                grids += [grid_1, grid_2, grid_3]
                grid_1, grid_2, grid_3 = [], [], []

        def all_unique(segments):
            for segment in segments:
                filled = [c for c in segment if c != "."]
                if len(filled) != len(set(filled)):
                    return False
            return True

        return all_unique(board) and all_unique(cols) and all_unique(grids)
            



        