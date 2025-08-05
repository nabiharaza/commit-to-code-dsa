# Last updated: 8/5/2025, 2:54:46 PM
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transdict = self.createDict(transactions)
        return self.invalidCheck(transdict)
    
    def invalidCheck(self, transdict):
        invalid = set()
        for k, v in transdict.items():
            for item in range(len(v)):
                if int(v[item][2]) > 1000:
                    invalid.add(','.join(v[item]))
                for i in range(len(v)):
                    if i != item:
                        if abs(int(v[i][1]) - int(v[item][1])) <= 60 and v[i][3] != v[item][3]:
                            invalid.add(','.join(v[item]))
                            invalid.add(','.join(v[i]))
        return list(invalid)

    def createDict(self, transactions):
        transdict = dict()
        for ele in transactions:
            ele = ele.split(',')
            if ele[0] not in transdict:
                transdict[ele[0]] = []
            transdict[ele[0]].append([ele[0], ele[1], ele[2], ele[3]])
        return transdict