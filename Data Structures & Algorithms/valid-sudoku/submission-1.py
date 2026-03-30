class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        duplicates_set = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":

                    SQAURE_ROW, SQUARE_COL = r // 3, c // 3
                    row = (("row", r), board[r][c])
                    col = (("col", c), board[r][c])
                    square = ((SQAURE_ROW, SQUARE_COL), board[r][c])

                    if row in duplicates_set or col in duplicates_set or square in duplicates_set:
                        return False

                    duplicates_set.add(row)
                    duplicates_set.add(col)
                    duplicates_set.add(square)


        # check duplicates for each row
        # for r in range(9):
        #     row_nums = set()
        #     for c in range(9):
        #         if board[r][c] != ".":
        #             if board[r][c] in row_nums:
        #                 return False
        #             else:
        #                 row_nums.add(board[r][c])

        # # check duplicates for each column
        # for c in range(9):
        #     column_nums = set()
        #     for r in range(9):
        #         if board[r][c] != ".":
        #             if board[r][c] in column_nums:
        #                 return False
        #             else:
        #                 column_nums.add(board[r][c])

        # # check duplicates for each 3x3
        # square_num_sets = {}
        # for r in range(len(board)):
        #     for c in range(len(board[0])):
        #         ROW, COL = r // 3, c // 3
        #         if board[r][c] != ".":
        #             if (ROW, COL) in square_num_sets:
        #                 if board[r][c] in square_num_sets[(ROW, COL)]:
        #                     return False
        #                 else:
        #                     square_num_sets[(ROW, COL)].add(board[r][c])
        #             else:
        #                 square_num_sets[(ROW,COL)] = set(board[r][c])

        return True