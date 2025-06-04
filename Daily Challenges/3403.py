class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        n = len(word)

        if numFriends == 1:
            return word


        best = ""

        for a in range(n):
            b_max = n - (numFriends - 1) + a

            if b_max > n:
                bmax = n


            if b_max > a:
                cand = word[a:b_max]
                if cand > best:
                    best = cand

        return best