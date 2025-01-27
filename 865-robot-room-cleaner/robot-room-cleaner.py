# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # clockwise: up, right, down, left
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]
        visited = set()

        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtracking(curr=(0,0), d=0):
            if curr in visited:
                return
            visited.add(curr)
            robot.clean()
            for i in range(4):
                new_d = (d + i) % 4
                nxt = (curr[0] + directions[new_d][0], curr[1] + directions[new_d][1])
                if nxt not in visited and robot.move():
                    backtracking(nxt, new_d)
                    goBack()
                robot.turnRight()
        
        backtracking()

