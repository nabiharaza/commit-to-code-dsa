# Last updated: 8/5/2025, 2:56:54 PM
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph_dict = dict()
        result = ""
        for w in string.punctuation:
            paragraph = paragraph.replace(w, " ")
        # for w in paragraph:
        #     if w not in string.punctuation:
        #         result += w

        paragraph = paragraph.split(" ")

        for word in paragraph:
            if word not in banned and word != '':
                if word in paragraph_dict.keys():
                    paragraph_dict[word] += 1
                else:
                    paragraph_dict[word] = 1
        print(paragraph_dict)

        high_score = 0
        high_key = None
        for word, count in paragraph_dict.items():
            if count > high_score:
                high_score = count
                high_key = word
        return high_key