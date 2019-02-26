class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.opt = []
        candidates.sort()
        self.backtrack(candidates,target,0,[])
        return self.opt
    
    def backtrack(self,candidates,target,start,val):
        if target == 0:
            self.opt.append(val[:])
        for i in range(start,len(candidates)):
            if target > 0:
                val.append(candidates[i])
            else:
                break
            self.backtrack(candidates,target-candidates[i],i,val)
            val.pop()