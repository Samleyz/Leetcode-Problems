class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(dist)
        for k in range(n):
            dist[k] = float(dist[k]) / float(speed[k])

        dist = sorted(dist)
        print(dist)
        for i in range(n):
            if i >= dist[i]:
                return i
        return n
