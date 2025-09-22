class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        for log in logs:
            id_exec = log.split(":")
            idx, time = int(id_exec[0]), int(id_exec[2])
            if id_exec[1] == "start":
                if stack:
                    result[stack[-1][0]] += time - stack[-1][1]
                stack.append((idx, time))
            else:
                if stack and stack[-1][0] == idx:
                    result[stack[-1][0]] += time - stack[-1][1] + 1
                    stack.pop()
                    if stack:
                        stack[-1] = (stack[-1][0], time+1)
                else:
                    print("Error!")
                    break
            
        return result
        