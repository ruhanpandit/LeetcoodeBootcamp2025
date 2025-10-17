# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        nums = []
        curr = head
        while (curr):
            nums.append(curr)
            curr = curr.next
        
        left, right = 0, len(nums)-1
        while (left < right):
            nums[left].next = nums[right]
            left += 1
            
            if (left == right):
                break

            nums[right].next = nums[left]
            right -= 1
        
        nums[left].next = None