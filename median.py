def median_array(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    if m == 0:
        if n % 2 == 1:
            return nums2[n // 2]
        else:
            return (nums2[n // 2 - 1] + nums2[n // 2]) / 2
    s, e = 0, m
    half = (m + n + 1) // 2
    while s <= e:
        i = (s + e) // 2
        j = half - i
        nums1_lt = nums1[i-1] if i > 0 else float('-inf')
        nums1_rt = nums1[i] if i < m else float('inf')
        nums2_lt = nums2[j-1] if j > 0 else float('-inf')
        nums2_rt = nums2[j] if j < n else float('inf')
        if nums1_lt <= nums2_rt and nums2_lt <= nums1_rt:
            if (m + n) % 2 == 1:
                return max(nums1_lt, nums2_lt)
            else:
                return (max(nums1_lt, nums2_lt) + min(nums1_rt, nums2_rt)) / 2
        elif nums1_lt > nums2_rt:
            e = i - 1
        else:
            s = i + 1
    raise ValueError("Input arrays not sorted")

nums1 = [1, 3]
nums2 = [2]
result = median_array(nums1, nums2)
print(f"Median: {result}") 