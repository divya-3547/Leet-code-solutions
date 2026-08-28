class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result=0
        for i in range(n):
            x=start+2*i
            result^=x
        return result
