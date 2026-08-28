class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        n1=num
        while n1>0:
            digit=n1%10
            if num%digit==0:
                count+=1
            n1=n1//10
        return count

