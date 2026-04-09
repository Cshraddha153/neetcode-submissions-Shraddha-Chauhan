class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2=0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow




















        # slow, fast = 0, 0
        # while True:
        #     slow = nums[slow] #1 2
        #     print("slow", slow)
        #     fast = nums[nums[fast]] #2 2
        #     print("fast", fast)
        #     if slow==fast:
        #         break
        
        # slow2 = 0
        # while True:
        #     slow = nums[slow]  #3   2
        #     print(slow)
        #     slow2 = nums[slow2] #1  2
        #     print(slow2)
        #     if slow ==  slow2:
        #         return slow