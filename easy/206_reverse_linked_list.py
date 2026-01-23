from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"

fifth = ListNode(val=5, next=None)
fourth = ListNode(val=4, next=fifth)
third = ListNode(val=3, next=fourth)
second = ListNode(val=2, next=third)
first = ListNode(val=1, next=second)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
    
        if not head.next:
            return head


        prev = None
        current = head

        while current:
            next_temp = current.next
            current.next = prev 
            prev = current
            current = next_temp

        return prev

head = [first, second, third, fourth, fifth]

s = Solution()
print(s.reverseList(first))

