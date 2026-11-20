class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        bracket_list        = []
        for bracket in s:
            if bracket == "(":
                bracket_list.append(bracket)
            elif bracket == ")" and bracket_list and bracket_list[-1] == "(":
                bracket_list.pop()
            elif bracket == "{":
                bracket_list.append(bracket)
            elif bracket == "}" and bracket_list and bracket_list[-1] == "{":
                bracket_list.pop()
            elif bracket == "[":
                bracket_list.append(bracket)
            elif bracket == "]" and bracket_list and bracket_list[-1] == "[":
                bracket_list.pop()
            else:
                return False
        if not bracket_list:
            return True
        return False