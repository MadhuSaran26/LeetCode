class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        log = defaultdict(list)
        for time, holder in zip(keyTime, keyName):
            hour, minutes = time.split(":")
            minutes = int(hour)*60 + int(minutes)
            log[holder].append(minutes)
        
        result = []

        for holder, stamps in log.items():
            if len(stamps) < 3:
                continue
            stamps.sort()
            for idx in range(len(stamps)-2):
                if stamps[idx+2] - stamps[idx] <= 60:
                    result.append(holder)
                    break
        
        result.sort()
        return result


        