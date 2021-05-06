from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        if not nums1:
            nums1.extend(nums2[:n])
            return

        if not nums2:
            result = nums1[:m]
            nums1.clear()
            nums1.extend(result)
            return

        m_index = 0
        n_index = 0

        while m_index < m or n_index < n:
            if m_index < m and n_index < n and nums1[m_index] <= nums2[n_index]:
                result.append(nums1[m_index])
                m_index += 1
            elif n_index < n - 1:
                result.append(nums2[n_index])
                n_index += 1
            else:
                result.append(nums2[n_index])
                m_index += 1
        nums1 = result
        print(nums1)

    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     if not nums1:
    #         nums1.extend(nums2[:n])
    #         return
    #
    #     if not nums2:
    #         result = nums1[:m]
    #         nums1.clear()
    #         nums1.extend(result)
    #         return
    #
    #     result = nums1[:m]
    #     result.extend(nums2[:n])
    #     nums1.clear()
    #     nums1.extend(result)
    #     nums1.sort()
    #     print(nums1)


sol = Solution()
sol.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
sol.merge(nums1=[1], m=1, nums2=[], n=0)
sol.merge(nums1=[2, 0], m=1, nums2=[1], n=1)
