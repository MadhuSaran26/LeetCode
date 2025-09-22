class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        for log in logs:
            idx, etype, time = log.split(":")
            idx, time = int(idx), int(time)
            if etype == "start":
                if stack:
                    # pause current running function
                    result[stack[-1][0]] += time - stack[-1][1]
                stack.append((idx, time))
            else:
                if stack and stack[-1][0] == idx:
                    fid, start_time = stack.pop()
                    result[fid] += time - start_time + 1
                    if stack:
                        stack[-1] = (stack[-1][0], time+1)
                else:
                    print("Error!")
                    break
            
        return result
        