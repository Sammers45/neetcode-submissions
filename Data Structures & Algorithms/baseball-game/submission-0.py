class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for ops in operations:
            if ops == "+":
                record.append(record[-1] + record[-2])
            elif ops == "C":
                record.pop()
            elif ops == "D":
                record.append(2 * record[-1])
            else:
                record.append(int(ops))
        return sum(record)
            

        