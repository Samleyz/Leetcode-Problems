import numpy as np
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # Get the number of rows and columns of the original matrix
        m, n = len(mat), len(mat[0])
        
        # Check if reshaping is possible
        if m * n != r * c:
            return mat  # Return the original matrix if reshaping is not possible
        else:
            # Flatten the matrix and reshape it into the new dimensions
            flattened = np.array(mat).flatten()  # Flatten the matrix
            reshaped = flattened.reshape(r, c)  # Reshape to r x c
            return reshaped.tolist()  # Convert back to list of lists for a matrix-like output

    
    
