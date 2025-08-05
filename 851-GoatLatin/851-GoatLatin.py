# Last updated: 8/5/2025, 2:56:49 PM
class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []
        for i, w in enumerate(S.split(' ')):
            if w[0] not in list('aeiouAEIOU'):
                w = w[1:] + w[0]
            res.append(w + 'ma' + 'a' * (i + 1))
        return ' '.join(res)