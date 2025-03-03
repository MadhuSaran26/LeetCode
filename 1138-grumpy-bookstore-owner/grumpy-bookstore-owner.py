class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        satisfied_customers = 0
        for idx, grumpy_elem in enumerate(grumpy):
            if grumpy_elem == 0:
                satisfied_customers += customers[idx]
        
        add_satisfied_customers = 0
        left = 0
        new_satisfied = 0
        for right in range(n):
            while right-left+1 > minutes:
                add_satisfied_customers = max(add_satisfied_customers, new_satisfied)
                new_satisfied -= customers[left] * grumpy[left]
                left += 1
            new_satisfied += customers[right] * grumpy[right]
            
        add_satisfied_customers = max(add_satisfied_customers, new_satisfied)
        
        return satisfied_customers + add_satisfied_customers
            
                    
        