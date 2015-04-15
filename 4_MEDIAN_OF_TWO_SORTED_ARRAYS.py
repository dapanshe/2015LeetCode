class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        k = len(A) + len(B)
        if k%2 == 1:
            return self.findKthElementInTwoSortedArrays(A, B, (k+1)/2)
        else:
            left = self.findKthElementInTwoSortedArrays(A, B, k/2)
            right = self.findKthElementInTwoSortedArrays(A, B, k/2+1)
            return (left + right)/2.0
                         

    def findKthElementInTwoSortedArrays(self, a, b, k):
        if len(a) > len(b):
            a, b = b, a
        if len(a) == 0:
            return b[k-1]
        if k == 1:
            return min(a[0],b[0])
        if len(a) < (k - 1)/ 2.0:
            a_index = len(a) - 1
            b_index = k - len(a) - 1
        else:
            if k % 2== 0:
                a_index = k/2 - 1
                b_index = k/2 - 1
            else:
                a_index = (k-1)/2 - 1
                b_index = (k+1)/2 - 1
        if a[a_index] == b[b_index]:
            return a[a_index]
        elif a[a_index] < b[b_index]:
            return self.findKthElementInTwoSortedArrays(a[a_index+1:], b[:b_index+1], k-a_index-1)
        else:
            return self.findKthElementInTwoSortedArrays(a[:a_index+1], b[b_index+1:], k-b_index-1)
