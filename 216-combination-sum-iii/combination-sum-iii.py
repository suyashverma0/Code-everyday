class Solution:
    def solve(self,last,total,subset,result,n,k):
        if total==n and len(subset)==k:
            result.append(subset.copy())
            return
        if total>n or len(subset)>k:
            return
        
        for i in range(last,10):
            Sum = total+i
            subset.append(i)
            self.solve(i+1,Sum,subset,result,n,k)
            subset.pop()

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result=[]
        self.solve(1,0,[],result,n,k)
        return result
        