class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n1=n
        prod=1
        while(n1>0):
            digit=n1%10
            prod=prod*digit
            n1=n1//10
        n1=n
        sum=0
        while(n1>0):
            digit=n1%10
            sum=sum+digit
            n1=n1//10
        return (prod-sum)

