class Solution(object):
    def capitalizeTitle(self, title):
        result = []
        words = title.split()
        for word in words:
            if len(word)<= 2:
                result.append(word.lower())
            else:
                result.append(word.capitalize())
        return " ".join(result)            