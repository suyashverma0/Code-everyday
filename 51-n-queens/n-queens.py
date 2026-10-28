class Solution:
    def solve(self,col,board,leftrow,lowerBound,upperbound,ans,n):
        if col==n:
            ans.append(board[:])
            return
        for row in range(n):
            if(leftrow[row]==0 and lowerBound[row+col] == 0 and upperbound[n-1+col-row] == 0):
                board[row]= board[row][:col]+"Q"+board[row][col+1:]
                leftrow[row]=1
                lowerBound[row+col]=1
                upperbound[n-1+col-row]=1
                self.solve(col+1,board,leftrow,lowerBound,upperbound,ans,n)
                board[row]= board[row][:col]+"."+board[row][col+1:]
                leftrow[row]=0
                lowerBound[row+col]=0
                upperbound[n-1+col-row]=0



            











    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = ["."*n for _ in range(n)]
        leftrow = [0]*n
        lowerBound=[0]*(2*n-1)
        upperbound=[0]*(2*n-1)
        self.solve(0,board,leftrow,lowerBound,upperbound,ans,n)
        return ans
