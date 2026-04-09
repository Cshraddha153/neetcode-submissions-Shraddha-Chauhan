class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows-1
        #row find
        while top <= bot:
            rows = ( top + bot)//2
            if matrix[rows][-1]<target:
                top = rows + 1
            elif matrix[rows][0]>target:
                bot = rows - 1
            else:
                break
        
        if not top<=bot:
            return False


        l, r = 0, cols
        print(rows)
        rows = (top + bot)//2
        print(rows)
        while l<=r:
            m = (l + r)//2
            if matrix[rows][m] == target:
                return True
            elif matrix[rows][m]> target:
                r = m -1
            else:
                l=m+1
        return False

        # row = len(matrix)
        # col = len(matrix[0])
        # top, bot = 0, row-1
        # # find row in which soln exists
        # while top <= bot:
        #     row = top + (bot-top)//2
        #     if matrix[row][-1]<target:
        #         top = row + 1
        #     elif matrix[row][0]>target:
        #         bot = row - 1
        #     else:
        #         break

        # if not (top<=bot):
        #     return False

        # # find col soln exist
        # rows = (top + bot)//2
        # l, r = 0, col
        # while l <= r:
        #     mid = l + (r-l)//2
        #     if matrix[row][mid] == target:
        #         return True
        #     elif matrix[row][mid] > target:
        #         r = mid -1
        #     else:
        #         l = mid + 1
        # return False









