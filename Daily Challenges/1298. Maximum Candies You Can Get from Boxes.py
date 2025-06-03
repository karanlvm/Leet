class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        
        n = len(status)
        # To track what boxes we have
        has_box = [False] * n
        # Which boxes we have the keys for
        have_key = [False] * n
        # Track which boxes we have already opened
        used = [False] * n

        queue = deque()

        totalCandies = 0

        for b in initialBoxes:
            if not has_box[b]:
                has_box[b] = True
                if status[b] == 1:
                    queue.append(b)

        while queue:
            box_idx = queue.popleft()

            if used[box_idx]:
                continue

            used[box_idx] = True
            totalCandies += candies[box_idx]


            for k in keys[box_idx]:
                if not have_key[k]:
                    have_key[k] = True

                    if has_box[k] and not used[k]:
                        queue.append(k)

            for new_box in containedBoxes[box_idx]:
                if not has_box[new_box]:
                    has_box[new_box] = True


                    if status[new_box] == 1 or have_key[new_box]:
                        queue.append(new_box)

        return totalCandies
