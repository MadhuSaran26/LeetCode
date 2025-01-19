# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = 1
        sum_elem = 0
        sum_elemdepth = 0

        #sum(elem*maxDepth - elem*depth + elem)
        #sum(elem) + sum(elem)*maxDepth - sum(elem*depth)

        def getDepth(element, depth=0):
            nonlocal max_depth, sum_elem, sum_elemdepth
            depth += 1
            if element.isInteger():
                sum_elem += element.getInteger()
                sum_elemdepth += element.getInteger() * depth
                max_depth = max(max_depth, depth)
            else:           
                for elem in element.getList():
                    getDepth(elem, depth)

        for nested in nestedList:
            getDepth(nested)
        
        result = sum_elem + sum_elem * max_depth - sum_elemdepth

        return result

