class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()

        n = len(nums1)
        if n % 2 == 0:
            return (nums1[int(n/2) - 1] + nums1[int(n/2)])/2
        else:
            return nums1[n//2]

        # n, m = len(nums1), len(nums2)
        # if (n + m) % 2 == 0:
        #     l, u = (n + m) / 2 - 1, (n + m) / 2
        #     i = 0

        #     while n > 0 and m > 0:
        #         x, y = nums1.pop(0), nums1.pop(0)
        
        # else:
        #     l, u = (n + m) // 2, None


        