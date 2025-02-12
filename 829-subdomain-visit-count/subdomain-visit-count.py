class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = Counter()
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            fragments = domain.split(".")
            for idx in range(len(fragments)):
                result[".".join(fragments[idx:])] += count
        
        return [f"{count} {domain}" for domain, count in result.items()]
        