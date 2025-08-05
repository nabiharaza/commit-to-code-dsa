# Last updated: 8/5/2025, 2:52:43 PM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        characters = set()
        for i in sentence:
            characters.add(i)
        if len(characters) == 26:
            return True
        return False
        