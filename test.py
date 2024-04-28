def productExceptSelf(nums):
    res = [1] * len(nums)

    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]
    
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]


    print(res)
    return res



# 3a

# O(1)
z = 0
# O(1)
n = None

# O(n)
for j in range(1,n):
    # O(1)
    q = 0
    s = j * j
    # O()
    while q <= s:
        q += 5
        z += q

