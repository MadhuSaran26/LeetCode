class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        simple_path = []
        for i in range(len(path_list)):
            if path_list[i] == "" or path_list[i] == ".":
                continue
            if path_list[i] == "..":
                if simple_path:
                    simple_path.pop()
                continue
            simple_path.append(path_list[i])
        
        return "/" + "/".join(simple_path)
        