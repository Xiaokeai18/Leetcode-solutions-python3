class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.opt = []
        candidates.sort()
        self.backtrack(candidates,target,[])
        return self.opt
    
    def backtrack(self,candidates,target,val):
        if target == 0:
            if val[:] not in self.opt:
                self.opt.append(val[:])
        for i in range(len(candidates)):
            if target > 0:
                val.append(candidates[i])
            else:
                break
            self.backtrack(candidates[i+1:],target-candidates[i],val)
            val.pop()