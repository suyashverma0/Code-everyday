class Solution:
    def solve(self,index,total,subset,result,nums):
        if total ==0:
            result.append(subset.copy())
            return
        elif total<0:
            return
        if index>=len(nums):
            return
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            Sum = total-nums[i]
            self.solve(i+1,Sum,subset,result,nums)
            subset.pop()

        
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        candidates.sort()
        subset = []
        self.solve(0,target,subset,result,candidates)

        return list(result)
        