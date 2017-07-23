class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
       
        pa = [[] for i in range(numRows)]
        for i in range(numRows):
            pa[i] = [1 for j in range(i+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                pa[i][j] = pa[i-1][j-1] + pa[i-1][j]
        return pa
