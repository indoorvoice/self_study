class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_1 = str(bin(x))[2:]
        bin_2 = str(bin(y))[2:]
        
        if len(bin_1) < len(bin_2):
            bin_1 = bin_1.rjust(len(bin_2), '0')
        if len(bin_2) < len(bin_1):
            bin_2 = bin_2.rjust(len(bin_1), '0')
        
        ham_distance = 0
        for i in range(len(bin_1)):
            if bin_1[i] != bin_2[i]:
                ham_distance += 1
        
        return(ham_distance)
