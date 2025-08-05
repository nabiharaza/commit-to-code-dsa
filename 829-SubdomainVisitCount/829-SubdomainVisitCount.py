# Last updated: 8/5/2025, 2:56:55 PM
class Solution:
    visitedDomains = dict()

    def subdomainVisits(self, cpdomains):
        self.visitedDomains = dict() 
        for cp in cpdomains:
            cp = cp.split()
            count = int(cp[0])
            cp = cp[1]

            while cp != None:

                if cp in self.visitedDomains:
                    self.visitedDomains[cp] += count
                else:
                    self.visitedDomains[cp] = count

                cp_new = cp.split(".", 1)[-1]
                if cp_new == cp:
                    break
                else:
                    cp = cp_new

        visitedList = list()

        for key, val in self.visitedDomains.items():
            visitedList.append(str(val) + " " + key)
        return visitedList
        