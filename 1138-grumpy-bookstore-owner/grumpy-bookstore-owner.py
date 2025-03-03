class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        grumpy_count = Counter(grumpy)
        if 1 not in grumpy_count:
            return sum(customers)
        
        satisfied_customers = 0
        for idx, grumpy_elem in enumerate(grumpy):
            if grumpy_elem == 0:
                satisfied_customers += customers[idx]
        max_satisfied_customers = satisfied_customers

        for left in range(0, n-minutes+1):
            window = grumpy[left:left+minutes]
            new_satisfied = satisfied_customers
            for idx, win_elem in enumerate(window):
                if win_elem == 1:
                    new_satisfied += customers[left+idx]
            
            max_satisfied_customers = max(max_satisfied_customers, new_satisfied)
        
        return max_satisfied_customers
            
                    
        