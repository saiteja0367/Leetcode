class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank=0
        start=0
        gas_sum=sum(gas)
        cost_sum=sum(cost)
        if gas_sum<cost_sum:
            return -1
        for i in range(len(gas)):
            tank+=gas[i]-cost[i]
            if tank<0:
                start=i+1
                tank=0
        return start

        