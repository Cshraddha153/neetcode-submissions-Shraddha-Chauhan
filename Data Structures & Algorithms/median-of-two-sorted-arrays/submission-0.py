class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A)-1
        while True:
            i = (l + r)//2 # A  smaller
            j =  (half - i - 2)  # B bigger

            Aleft = A[i] if i>=0 else float("-infinity")
            Aright = A[i+1] if i+1<len(A) else float("infinity")
            Bleft = B[j] if j>=0 else float("-infinity")
            Bright = B[j+1] if j+1<len(B) else float("infinity")

            if Bleft<=Aright and Aleft<=Bright:
                if total % 2: # even
                    return  min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Bright, Aright))/2

            elif Aleft>Bright:
                    r = i - 1
            else:
                    l = i + 1



