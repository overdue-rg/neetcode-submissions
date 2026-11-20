class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_list = []
        total_sum = 0
        for op in operations:
            if op.isdigit() or "-" in op:
                number = int(op)
                score_list.append(number)
                total_sum += number
            elif op == "+":
                the_sum = score_list[-1] + score_list[-2]
                score_list.append(the_sum)
                total_sum += the_sum
            elif op == "D":
                D_sum = score_list[-1] * 2
                score_list.append(D_sum)
                total_sum += D_sum
            elif op == "C":
                total_sum -= score_list[-1]
                score_list.pop()
        return total_sum