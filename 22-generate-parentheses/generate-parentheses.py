class Solution:
    def solve(self,index,total,brackets,result):
        if index == len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return
        if total>len(brackets)//2:
            return
        elif total <0:
            return
        
        brackets[index]="("
        Sum = total+1
        self.solve(index+1,Sum,brackets,result)
        brackets[index]=")"
        Sum = total-1
        self.solve(index+1,Sum,brackets,result)
    def generateParenthesis(self, n: int) -> list[str]:
        brackets = [""]*(n*2)
        result = []
        self.solve(0,0,brackets,result)
        return result
        